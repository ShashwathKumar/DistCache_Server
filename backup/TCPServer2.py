from socket import *
import urllib, urllib2
import os.path
import re

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
cachePath = "./cache/"
size = 2048
while True:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(2048)
	msg = message.decode()
	print msg
	#print addr
	first = msg.find('http')
	last  = msg.find(' ', first+1)
	url = msg[first: last]
	print "-----------------------------"
	print url
	if not url:
		continue
	urlFile = re.sub('[^A-Za-z0-9_\\.]','-',url)
	if not os.path.isfile(cachePath+urlFile):
		f = open(cachePath+urlFile, 'w+')
		try:
			fileName = urllib2.urlopen(url)
			chunk = fileName.read(size)
			while chunk:
				f.write(chunk)
				chunk = fileName.read(size)
			f.close()
			#urllib.urlretrieve(url, urlFile) 
		except urllib2.HTTPError:
			continue
	f = open(cachePath+urlFile, 'rb')
	html = f.read(size)
	#print html
	connectionSocket.send("HTTP/1.1 200 OK\r\n"+
			
	# 		#"Date: Wed, 11 Apr 2012 21:29:04 GMT\n"+
	# 		#"Server: Python/6.6.6 (custom)\n"+
			"Content-Type: text/html\r\n"+
			"\r\n")

	# '''
	# 		"Cache-Control:no-cache, must-revalidate\n"+
	# 		"Connection:keep-alive\n"+
	# 		"Date:Mon, 31 Oct 2016 23:53:24 GMT\n"+
	# 		'ETag:"56564d14-21e16"\n'+
	# 		"Last-Modified:Thu, 26 Nov 2015 00:06:44 GMT\n"+
	# 		"Server:nginx\n")
	# '''
	while html:
		print html
		connectionSocket.send(html)
		html = f.read(size)
	f.close()
connectionSocket.shutdown()
connectionSocket.close()
