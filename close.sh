#!/bin/bash
#var=$(ps -ef | grep TCP | cut -d' ' -f1)
#var=$(ps -ef | grep "TCP" | awk '{print $2}')
#var=$(ps -ef | awk '/[T]CP/{print $2}')
#echo $var
#var=$(ps au | grep "TCPServer.py" | cut -d' ' -f10)
var=$(ps -ef | grep "TCPServer.py")
echo $var
