import socket
from Database import Database
from Parser import handle_client
from BookingDatabase import BookingDatabase
from book import Book
from user import User


HOST = '127.0.0.1'
PORT = 65432
database=Database("users.txt")
bookingDB=BookingDatabase("booking.txt")

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
            
            login, password = message.split(":")
            new_user = User(login, password)
            database.write(new_user)
            conn.send(("Account created!").encode( 'utf-8'))
              
        if "Entrance" in command:
            
            if database.searchfor(message):
                conn.send(("Accepted!").encode('utf-8'))
            else: 
                
                conn.send(("Declined!").encode('utf-8'))
         
        if "NewBooking" in command:
           
            name, phone, time, notes = message.split(",")
            new_book=Book(name, phone, time, notes)
            bookingDB.write(new_book)             
            conn.send(("Booked!").encode('utf-8'))
              
            

if __name__ == "__main__":
    main()



