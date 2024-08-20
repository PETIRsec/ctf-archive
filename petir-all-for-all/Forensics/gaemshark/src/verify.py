import socket
import threading

def handle_client(client_socket):
    try:
        client_socket.send("Verify your answer.\n".encode('utf-8'))

        questions = [
            "Is the phone rooted? [yes/no]: ",
            "What is the name of APK for rooting? [lowercase]: ",
            "What is the ransomware package name? [com.abc.xyz]: ",
            "Timestamp the database file is encrypted (MM/DD hh:mm:ss): ",
            "What is the decryption key? ",
            "What is the password for web login? "
        ]
        answers = [
            "yes",
            "magisk",
            "com.crydroid",
            "08/14 00:37:11",
            "05SIrOT7Lp536aap",
            "kakean-ayag"
        ]

        for i in range(len(questions)):
            client_socket.send(questions[i].encode('utf-8'))

            data = client_socket.recv(1024).strip().decode("utf-8")
            print(f"Received answer: {data}")

            if data != answers[i]:
                client_socket.sendall(b"Incorrect answer. Connection closing.")
                print("Incorrect answer. Closing connection with client.")
                return
        
        client_socket.sendall(b"PETIR{n3v3r_trust_m4l1c10u5_4pk}")
        print("All answers correct. Success message sent.")
    
    except Exception as e:
        print("An error occurred while handling the client:", e)
    
    finally:
        client_socket.close()
        print("Client connection closed.")

def create_server(host, port):
    server_socket = None
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #server_socket.settimeout(20)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server is listening on {host}:{port}")
        
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            client_socket.settimeout(60)
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    except Exception as e:
        print("An error occurred with the server:", e)
    
    finally:
        # Close the server socket
        if server_socket:
            server_socket.close()

create_server('0.0.0.0', 4437)  
