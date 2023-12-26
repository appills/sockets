import socket
import ssl

# Server settings
HOST = '127.0.0.1'
PORT = 12345

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Wrap the socket with TLS
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
ssl_connection = context.wrap_socket(client_socket)
print(ssl_connection.cipher)
# Send data to the server
ssl_connection.sendall(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")

# Receive the response from the server
response = ssl_connection.recv(1024)
print(f"Received response from server: {response.decode()}")

# Close the connection
ssl_connection.close()
client_socket.close()
