from socket import *
import urllib2
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#url = "https://pixabay.com/static/uploads/photo/2013/10/18/09/15/flower-197343_960_720.jpg"
#url = "https://en.wikipedia.org/wiki/Flower"
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
	try:
		fileName = urllib2.urlopen(url)
	except urllib2.HTTPError:
		continue
	html = fileName.read(size)
	#print html
	connectionSocket.send("HTTP/1.1 200 OK\n"+
			
			#"Date: Wed, 11 Apr 2012 21:29:04 GMT\n"+
			#"Server: Python/6.6.6 (custom)\n"+
			"Content-Type: image/jpg\n")

	'''
			"Cache-Control:no-cache, must-revalidate\n"+
			"Connection:keep-alive\n"+
			"Date:Mon, 31 Oct 2016 23:53:24 GMT\n"+
			'ETag:"56564d14-21e16"\n'+
			"Last-Modified:Thu, 26 Nov 2015 00:06:44 GMT\n"+
			"Server:nginx\n")
	'''
	while html:
		print html
		connectionSocket.send(html)
		html = fileName.read(size)
connectionSocket.close()
