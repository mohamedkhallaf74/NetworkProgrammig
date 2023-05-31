
import socket

# Set the server address and port
server_address = ('localhost', 12345)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send data to the server
    message = b"Hello, server!"
    sock.sendto(message, server_address)

    # Receive the response from the server
    data, server = sock.recvfrom(4096)
    print("Response from server:", data.decode())
finally:
    # Close the socket
    sock.close()
