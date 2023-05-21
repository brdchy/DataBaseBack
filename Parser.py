import socket

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"connected: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"got message from {addr}: {data.decode('utf-8')}")
        # Здесь вы можете обработать полученные данные, например, сохранить их в базе данных
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
                
            
            
        




