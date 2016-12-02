from socket import *
import sys

host = 'www.google.com'
port = 80

IP_MTU_DISCOVER   = 10
IP_PMTUDISC_DONT  =  0  # Never send DF frames.
IP_PMTUDISC_WANT  =  1  # Use per route hints.
IP_PMTUDISC_DO    =  2  # Always DF.
IP_PMTUDISC_PROBE =  3  # Ignore dst pmtu.

url = sys.argv[1]
eth = 'eth1'

client = socket(AF_INET, SOCK_STREAM)
client.settimeout(15.0)
client.bind(('', 12000))
client.setsockopt(SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
client.setsockopt(SOL_SOCKET, 25, eth+'\0')
client.connect((host,port))

req = 'GET '+ url + ' HTTP/1.1\n\n'

client.send(req)

response = client.recv(1024)
print response
while response:
	response = client.recv(1024)
	if response:
		print response
	else:
		break
client.shutdown(1)
client.close()
