import socket

# Create socket
client_socket = socket.socket()

# Connect to server
client_socket.connect(('localhost', 12345))

print("Connected to server. Start chatting...")

while True:
    # Send message to server
    client_msg = input("You: ")
    client_socket.send(client_msg.encode())

    if client_msg.lower() == 'exit':
        break

    # Receive message from server
    server_msg = client_socket.recv(1024).decode()

    if server_msg.lower() == 'exit':
        print("Server ended the chat.")
        break

    print("Server:", server_msg)

client_socket.close()