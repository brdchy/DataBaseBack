import socket
from Database import Database
from Parser import handle_client

HOST = '127.0.0.1'
PORT = 65432
database=Database("users.txt")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"server is on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        command, message = handle_client(conn, addr)
        
        if "NewUser" in command:
            database.write(f"{message}")
            database.close()
            newmessage = "Account created!"
            conn.send(newmessage.encode('utf-8'))
              
        if "Entrance" in command:
            if database.searchfor(message):
                conn.send(("Accepted!").encode('utf-8'))
            else: conn.send(("Declined!").encode('utf-8'))
            database.close()

if __name__ == "__main__":
    main()


