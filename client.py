from socket import *
import sys

host = "www.google.com"
port = 80

IP_MTU_DISCOVER   = 10
IP_PMTUDISC_DONT  =  0  # Never send DF frames.
IP_PMTUDISC_WANT  =  1  # Use per route hints.
IP_PMTUDISC_DO    =  2  # Always DF.
IP_PMTUDISC_PROBE =  3  # Ignore dst pmtu.

url = sys.argv[1]
eth = sys.argv[2]

client = socket(AF_INET, SOCK_STREAM)
client.settimeout(2.0)
client.setsockopt(SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
client.setsockopt(SOL_SOCKET, 25, eth+'\0')
client.connect((host,port))

req = 'GET'+ url  + 'HTTP/1.1\r\n'+\
'Host: denninginstitute.com\r\n'+\
'Proxy-Connection: keep-alive\r\n'+\
'Cache-Control: max-age=0\r\n'+\
'Upgrade-Insecure-Requests: 1\r\n'+\
'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.59 Safari/537.36\r\n'+\
'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'+\
'Accept-Encoding: gzip, deflate, sdch\r\n'+\
'Accept-Language: en-US,en;q=0.8\r\n\r\n'

#client.send("GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n")
client.send(req)

response = client.recv(4096)
print response
while response:
	response = client.recv(4096)
	if response:
		print response
client.close()
