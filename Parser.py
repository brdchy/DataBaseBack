import socket
from Database import Database

HOST = '127.0.0.1'
PORT = 65432
database=Database("users.txt")


def handle_client(conn, addr):
    print(f"connected: {addr}")
    while True:
        data = conn.recv(1024)
        message=data.decode('utf-8')
        if not data:
            break
        print(f"got message from {addr}: {message}")
        command=""
        for i in message:
            if i=="?":
                break
            else: command+=i
        
        if "NewUser" in message:
            database.write(f"{message[len(command)+1:]}")
            
    conn.close()
    print(f"connection from {addr} closed")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"server is on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)

if __name__ == "__main__":
    main()
                
            
            
        




