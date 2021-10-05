import socket
import time

print("ba Bump")

UDP_IP = "10.0.2.15"
UDP_PORT = 5005

timestamp = time.time()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = str(timestamp)
message = str.encode(message)

sock.sendto(message, (UDP_IP, UDP_PORT))
