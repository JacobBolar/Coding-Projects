import socket

print("dum-da-DUM-dump")

UDP_IP = "10.0.2.15"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "calamity"
message = str.encode(message)

sock.sendto(message, (UDP_IP, UDP_PORT))
