from flask import Flask, request, jsonify, render_template, redirect, url_for, session, g
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from functools import wraps
import jwt
import datetime
import os
import hmac
import hashlib
import sqlite3
import json
import yaml
import logging
import random
import string
import shutil
from werkzeug.utils import secure_filename

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

app = Flask(__name__)
app.config['SECRET_KEY'] = generate_random_string(32)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
logging.basicConfig(level=logging.INFO)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'

REAL_JWT_SECRET = hashlib.sha256(os.urandom(128)).hexdigest()

UPLOAD_BASE_FOLDER = 'uploads'

class User(UserMixin):
    def __init__(self, id, username, role, api_token):
        self.id = id
        self.username = username
        self.role = role
        self.api_token = api_token

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('ctf.db')
    c = conn.cursor()
    user = c.execute(
        'SELECT id, username, role, api_token FROM users WHERE id = ?',
        (user_id,),
    ).fetchone()
    conn.close()

    if user:
        return User(user[0], user[1], user[2], user[3])
    return None

@app.before_request
def before_request():
    if 'PLAYER_ID' not in session:
        session['PLAYER_ID'] = generate_random_string(8)
    g.DATABASE_FILENAME = f"ctf_{session['PLAYER_ID']}.db"
    g.UPLOAD_FOLDER = os.path.join(UPLOAD_BASE_FOLDER, session['PLAYER_ID'])
    if not os.path.exists(g.DATABASE_FILENAME):
        init_db(g.DATABASE_FILENAME)
    if not os.path.exists(g.UPLOAD_FOLDER):
        os.makedirs(g.UPLOAD_FOLDER, exist_ok=True)

def init_db(database_filename):
    conn = sqlite3.connect(database_filename)
    c = conn.cursor()

    c.execute(
        '''CREATE TABLE IF NOT EXISTS configs
                 (id INTEGER PRIMARY KEY,
                  name TEXT UNIQUE,
                  content TEXT,
                  signature TEXT)'''
    )

    initial_config = {
        'app_name': "Spicy Storage",
        'debug': False,
        'remote_import': False,
        'allowed_extensions': ['.txt'],
        'max_file_size': 1024,
    }
    config_str = json.dumps(initial_config)
    initial_signature = generate_hmac(config_str, app.config['SECRET_KEY'])

    c.execute(
        "INSERT OR REPLACE INTO configs (name, content, signature) VALUES (?, ?, ?)",
        ('system', config_str, initial_signature),
    )

    conn.commit()
    conn.close()


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({'error': 'Authentication required'}), 401
        if current_user.role != 'admin_spicy':
            return jsonify({'error': 'Admin access required'}), 403
        return f(*args, **kwargs)
    return decorated_function

def generate_hmac(data, secret):
    return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()

def verify_jwt_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token:
            return jsonify({'message': 'Token required'}), 401

        try:
            data = jwt.decode(token, REAL_JWT_SECRET, algorithms=['HS256'])

            if not all(k in data for k in ['user_id', 'username', 'role']):
                return jsonify({'message': 'Invalid token format'}), 401

            conn = sqlite3.connect('ctf.db')
            c = conn.cursor()
            user = c.execute(
                'SELECT id, username, role FROM users WHERE id = ?',
                (data['user_id'],),
            ).fetchone()
            conn.close()

            if not user or user[1] != data['username'] or user[2] != data['role']:
                return jsonify({'message': 'Token validation failed'}), 401

            return f(*args, **kwargs)
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        except Exception:
            return jsonify({'message': 'Token validation error'}), 401

    return decorated

@app.route('/')
def index():
    return render_template('index.html', config=json.loads(sqlite3.connect(g.DATABASE_FILENAME).cursor().execute("SELECT content FROM configs WHERE name='system'").fetchone()[0]))

@app.route('/login', methods=['GET'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('login.html', config=json.loads(sqlite3.connect(g.DATABASE_FILENAME).cursor().execute("SELECT content FROM configs WHERE name='system'").fetchone()[0]))

@app.route('/login', methods=['POST'])
def login_post():
    try:
        data = request.get_json()
        username = data.get('username', '')
        password = data.get('password', '')

        conn = sqlite3.connect('ctf.db')
        c = conn.cursor()
        query = f"SELECT id, username, role, api_token FROM users WHERE username = '{username}' AND password = '{password}'"
        user = c.execute(query).fetchone()
        conn.close()

        if user:
            user_obj = User(user[0], user[1], user[2], user[3])
            login_user(user_obj)

            token = jwt.encode(
                {
                    'user_id': user[0],
                    'username': user[1],
                    'role': user[2],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                },
                REAL_JWT_SECRET,
            )

            response = jsonify({'message': 'Login successful'})
            response.set_cookie('auth_token', token)
            return response

    except Exception as e:
        return jsonify({'message': 'Error occurred!'}), 500

    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/api/config/update', methods=['POST'])
@verify_jwt_token
@admin_required
def update_config():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    class Config:
        pass

    try:
        data = request.get_json()
        config_data = data.get('config', {})

        protected_fields = ['remote_import', 'debug']
        for field in protected_fields:
            if field in config_data:
                return jsonify({'error': f'Cannot modify protected field: {field}'}), 403

        conn = sqlite3.connect(g.DATABASE_FILENAME)
        c = conn.cursor()

        current_config = c.execute(
            "SELECT content FROM configs WHERE name=?",
            ('system',),
        ).fetchone()

        if current_config:
            config_obj = Config()
            base_config = json.loads(current_config[0])

            for k, v in base_config.items():
                setattr(config_obj, k, v)

            for key, value in config_data.items():
                if key not in protected_fields:
                    setattr(config_obj, key, value)

            updated_config = config_obj.__dict__
            config_str = json.dumps(updated_config)
            signature = generate_hmac(config_str, app.config['SECRET_KEY'])

            c.execute(
                "UPDATE configs SET content=?, signature=? WHERE name=?",
                (config_str, signature, 'system'),
            )
            conn.commit()

            return jsonify({'message': 'Config updated', 'config': updated_config})
    finally:
        if 'conn' in locals():
            conn.close()

@app.route('/api/upload', methods=['POST'])
@verify_jwt_token
def upload_file():
    uploaded_filepath = None
    file = None
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        conn = sqlite3.connect(g.DATABASE_FILENAME)
        c = conn.cursor()
        config_data = c.execute(
            "SELECT content FROM configs WHERE name=?",
            ('system',),
        ).fetchone()
        conn.close()

        if not config_data:
            return jsonify({'error': 'Config not found'}), 500

        config = json.loads(config_data[0])
        allowed_extensions = config.get('allowed_extensions', [])
        max_size = int(config.get('max_file_size', 1024))

        file_content = file.read()
        if len(file_content) > max_size:
            return jsonify(
                {
                    'error': f'File size exceeds maximum allowed size of {max_size} bytes'
                }
            ), 400

        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in allowed_extensions:
            return jsonify({'error': 'File type not allowed'}), 400

        filename = secure_filename(file.filename)
        uploaded_filepath = os.path.join(g.UPLOAD_FOLDER, filename)

        with open(uploaded_filepath, 'wb') as f_out:
            f_out.write(file_content)
        print(f"File saved to: {uploaded_filepath}")

        if b'!!' in file_content:
            try:
                os.remove(uploaded_filepath)
                print(f"File removed: {uploaded_filepath}")
                return jsonify({'error': 'File contains restricted content'}), 400
            except Exception as e:
                print(f"Failed to remove file: {e}")
                try:
                    import subprocess
                    subprocess.call(['rm', '-f', uploaded_filepath])
                    print(f"Forcefully removed: {uploaded_filepath}")
                except Exception as ex:
                    print(f"Failed to forcefully remove file: {ex}")
                return jsonify({'error': 'Failed to remove malicious file'}), 500

        return jsonify(
            {'message': 'File uploaded successfully', 'path': uploaded_filepath}
        )

    except Exception as e:
        print(f"Upload error: {e}")
        if uploaded_filepath and os.path.exists(uploaded_filepath):
            try:
                os.remove(uploaded_filepath)
                print(f"Cleanup successful: {uploaded_filepath}")
            except Exception as e:
                print(f"Cleanup failed: {e}")
                try:
                    import subprocess
                    subprocess.call(['rm', '-f', uploaded_filepath])
                    print(f"Forcefully removed: {uploaded_filepath}")
                except Exception as ex:
                    print(f"Failed to forcefully remove file: {ex}")
        return jsonify({'error': str(e)}), 500
    finally:
        if file:
            file.close()

@app.route('/api/files', methods=['GET'])
@verify_jwt_token
def get_uploaded_files():
    try:
        files = []
        for root, dirs, filenames in os.walk(g.UPLOAD_FOLDER):
            for filename in filenames:
                files.append(filename)
        return jsonify(files), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/config/import', methods=['POST'])
@verify_jwt_token
@admin_required
def import_config():
    try:
        conn = sqlite3.connect(g.DATABASE_FILENAME)
        c = conn.cursor()

        current_config = c.execute(
            "SELECT content FROM configs WHERE name=?",
            ('system',),
        ).fetchone()

        if current_config:
            config = json.loads(current_config[0])
            if not config.get('remote_import', False):
                return jsonify({'error': 'Remote import not enabled'}), 403

        data = request.get_json()
        config_path = data.get('path', '')

        filename = secure_filename(os.path.basename(config_path))
        if not filename:
            return jsonify({'error': 'Invalid filename'}), 400

        config_path = os.path.join(g.UPLOAD_FOLDER, filename)
        file_ext = os.path.splitext(config_path)[1].lower()
        allowed_extensions = config.get('allowed_extensions', [])
        if file_ext not in allowed_extensions:
            return jsonify({'error': 'Invalid file type'}), 400

        try:
            with open(config_path, 'r') as f:
                yaml.load(f, Loader=yaml.Loader)
                return jsonify({'message': 'Config imported'})
        except Exception as e:
            return jsonify({'error': f'Failed to load config: {str(e)}'}), 400

    finally:
        if 'conn' in locals():
            conn.close()

@app.route('/api/read_file', methods=['GET'])
@verify_jwt_token
def read_file():
    try:
        file_name = request.args.get('file')
        if not file_name:
            return jsonify({'error': 'File name is required'}), 400

        file_path = os.path.join(g.UPLOAD_FOLDER, file_name)
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404

        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({'content': content}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred while reading the file: {str(e)}'}), 500

@app.route('/dashboard')
@login_required
def dashboard():
    conn = sqlite3.connect(g.DATABASE_FILENAME)
    c = conn.cursor()
    try:
        config_row = c.execute(
            "SELECT content FROM configs WHERE name='system'"
        ).fetchone()
        if config_row:
            config = json.loads(config_row[0])
        else:
            config = {'allowed_extensions': ['.txt'], 'max_file_size': 1024}
    except:
        config = {'allowed_extensions': ['.txt'], 'max_file_size': 1024}
    finally:
        conn.close()

    return render_template('dashboard.html', config=config)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

def create_shared_db():
    if os.path.exists('ctf.db'):
        try:
            os.remove('ctf.db')
            print("Shared database file removed.")
        except Exception as e:
            print(f"Error removing shared database: {e}")

    conn = sqlite3.connect('ctf.db')
    c = conn.cursor()

    c.execute(
        '''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                  username TEXT UNIQUE,
                  password TEXT,
                  role TEXT,
                  api_token TEXT)'''
    )

    admin_position = random.randint(0, 199)

    for i in range(200):
        if i == admin_position:
            create_random_user(c, role='admin_spicy')
        else:
            create_random_user(c)

    conn.commit()
    conn.close()

def create_random_user(c, role='user'):
    username = generate_random_string(8)
    password = generate_random_string(12)
    api_token = hashlib.sha256(os.urandom(16)).hexdigest()

    c.execute(
        "INSERT OR IGNORE INTO users (username, password, role, api_token) VALUES (?, ?, ?, ?)",
        (username, password, role, api_token),
    )

def clean_all():
    db_files = [f for f in os.listdir('.') if f.startswith('ctf_') and f.endswith('.db')]
    for db_file in db_files:
        try:
            os.remove(db_file)
            print(f"Removed database file: {db_file}")
        except Exception as e:
            print(f"Failed to remove database file {db_file}: {e}")

    if os.path.exists(UPLOAD_BASE_FOLDER):
        try:
            shutil.rmtree(UPLOAD_BASE_FOLDER)
            print(f"Removed upload folder: {UPLOAD_BASE_FOLDER}")
        except Exception as e:
            print(f"Failed to remove upload folder {UPLOAD_BASE_FOLDER}: {e}")

if __name__ == '__main__':
    clean_all()
    create_shared_db()
    app.run(host='0.0.0.0', port=4573, debug=False)
