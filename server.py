import socket
import ssl

# Server settings
HOST = '127.0.0.1'
PORT = 12345

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))
# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# Accept a connection and wrap it with TLS
connection, address = server_socket.accept()
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_connection = context.wrap_socket(connection, server_side=True)
print(ssl_connection.cipher)
# Receive data from the client
data = ssl_connection.recv(1024)
print(f"Received data from client: {data.decode()}")

# Send a response back to the client
ssl_connection.sendall(b"HTTP/1.1 200 OK\r\nHost: " + host.encode() + b"\r\n\r\n")

# Close the connection
ssl_connection.close()
server_socket.close()
