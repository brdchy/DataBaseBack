def handle_client(conn, addr):
    
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
        return command, f"{message[len(command)+1:]}"


    conn.close()
    print(f"connection from {addr} closed")


                
            
            
        




  