const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./db/sqlite.db');

// Function to create users table
const createUsersTable = () => {
    db.serialize(() => {
        db.run('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, profile_pic TEXT, role TEXT)');
    });
};

// Function to get user by username
const getUserByUsername = (username, callback) => {
    db.get('SELECT * FROM users WHERE username = ?', [username], callback);
};

// Function to create a new user
const createUser = (username, password, profile_pic, role, callback) => {
    db.run('INSERT INTO users (username, password, profile_pic, role) VALUES (?, ?, ?, ?)', [username, password, profile_pic, role], callback);
};

// Function to update a user's profile
const updateUserProfile = (userId, profile_pic, callback) => {
    db.run('UPDATE users SET profile_pic = ? WHERE id = ?', [profile_pic, userId], callback);
};

// Function to get all users
const getAllUsers = (callback) => {
    db.all('SELECT * FROM users', callback);
};

// Function to get user by ID
const getUserById = (id, callback) => {
    db.get('SELECT * FROM users WHERE id = ?', [id], callback);
};

// Function to update user details
const updateUserDetails = (id, username, profile_pic, password, callback) => {
    db.run('UPDATE users SET username = ?, profile_pic = ?, password = ? WHERE id = ?', [username, profile_pic, password, id], callback);
};

// Call the function to create users table on startup
createUsersTable();

// Export the database functions
module.exports = {
    getUserByUsername,
    createUser,
    updateUserProfile,
    getAllUsers,
    getUserById,
    updateUserDetails
};
