from socket import *
import thread
import urllib, urllib2
import os.path
import re

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
cachePath = "./cache/"
size = 2048
extDict = {}

while True:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(2048)
	msg = message.decode()
	print msg
	#print addr
	first = msg.find('http')
	last  = msg.find(' ', first+1)
	url = msg[first: last]
	reqType = ''
	print "-----------------------------"
	print url
	if not url:
		continue
	else:
		firstType = msg.find('Accept: ')
		lastType  = msg.find('\r\n',firstType)
		reqType   = msg[firstType+8: lastType]
		print reqType	
	urlFile = re.sub('[^A-Za-z0-9_\\.]','-',url)
	if not os.path.isfile(cachePath+urlFile):
		f = open(cachePath+urlFile, 'w+')
		try:
			fileName = urllib2.urlopen(url)
			extDict[url] = fileName.info().getheader('Content-Type')
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
	connectionSocket.send("HTTP/1.1 200 OK\r\n"+
			"Content-Type: "+extDict[url]+"\r\n"+
			"\r\n")

	while html:
		#print html
		connectionSocket.send(html)
		html = f.read(size)
	f.close()
	#connectionSocket.shutdown(socket.SHUT_RDWR)
	connectionSocket.close()
