import socket
import time

UDPIP =  "10.0.2.15"
UDPPORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDPIP, UDPPORT))

print("Heartbeat server started ...")

count = 1

while True:
	data, addr = sock.recvfrom(1024)
	
	try:
		time_str = time.ctime(float(data))
	except:
		print("bogus")
	else:
		log_str = str(count) + ": " + time_str + \
		", addr: " + addr[0] + ":" + str(addr[1])
	
		print(log_str)
	
		count += 1
