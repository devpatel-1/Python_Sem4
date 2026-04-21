import socket

# Create socket
server_socket = socket.socket()

# Bind and listen
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server waiting for connection...")

conn, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    
    if client_msg.lower() == 'exit':
        print("Client ended the chat.")
        break

    print("Client:", client_msg)

    # Send message to client
    server_msg = input("You: ")
    conn.send(server_msg.encode())

    if server_msg.lower() == 'exit':
        break

conn.close()
server_socket.close()