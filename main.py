import socket
from Database import Database
from Parser import handle_client
from BookingDatabase import BookingDatabase
from book import Book
from user import User
from TablesDatabase import TablesDatabase


HOST = '127.0.0.1'
PORT = 65432
database = Database("users.txt")
bookingDB = BookingDatabase("booking.txt")
tablesDB = TablesDatabase("tables.txt")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print(f"server is on {HOST}:{PORT}")   
    print(f"connected: {addr}")
    
    
    while True:
        
        command, message = handle_client(conn, addr)
        
        if "NewUser" in command:
            exists, user = database.searchfor(message)
            if not exists:
                login, password = message.split(":")
                new_user = User(login, password)
                database.write(new_user)
                database.close()
                conn.send(("Account created!").encode( 'utf-8'))
            else: conn.send(("Account exists!").encode( 'utf-8'))
              
        if "Entrance" in command:
            accessed, user = database.searchfor(message)
            if accessed:
                conn.send(("Accepted!").encode('utf-8'))
            else: 
                
                conn.send(("Declined!").encode('utf-8'))

        if "Admin" in command:
            accessed, user = database.searchfor(message)
            if accessed:        
                if "True" in user:
                    conn.send(("Admin entered!").encode('utf-8'))
                else: conn.send(("You don't have admin permissions").encode('utf-8'))        
            else:       
                conn.send(("Declined!").encode('utf-8'))
         
         
        if "NewBooking" in command:
           
            name, phone, table, time, notes = message.split(",")
            new_book=Book(name, phone, table, time, notes)
            if bookingDB.isfree(str(time)): 
                bookingDB.write(new_book)             
                conn.send(("T").encode('utf-8'))
            else:
                conn.send(("F").encode('utf-8'))

        if "UnloadUsers" in command:

            UnUsers = database.unload_users()
            conn.send((f"{UnUsers}").encode('utf-8'))
            
        if "UnloadTables" in command:
            
            UnTables = tablesDB.unload_tables()
            conn.send((f"{UnTables}").encode('utf-8'))
            
        if "DeleteUser" in command:
            exists = database.searchfor(message)
            if exists:
                database.delete_record(message)

                conn.send(("User deleted!").encode('utf-8'))
            else:
                conn.send(("User not found!").encode('utf-8'))
            

if __name__ == "__main__":
    main()



