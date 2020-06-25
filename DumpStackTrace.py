#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
import sys
import codecs
import os
import ntpath
import binascii

InputAddrFile = "addr.StackTrace"
InputNameFile = "name.StackTrace"
TimeStamp = "TimeStamp.txt"
Time = open(TimeStamp, 'r')
Time = Time.readline()
k = open("StackTrace_Output.cpp", 'w')
k.write("//------------------------------------------------\n")
k.write("//--- Fire Emblem: Fates Stack Trace\n")
k.write("//--- [Offset]: [Function Name]\n")
k.write("//" + Time[0:-1] + "\n")
k.write("//------------------------------------------------\n")
k.write("\n")

with open(InputAddrFile,"rb") as f:

	filesize = os.stat(InputAddrFile)
	filesize = filesize.st_size
	i = 1
	while( i < (filesize/8)):
		q = open(InputNameFile,"rb")
		CodeAddr = f.read(4)
		NameAddr = f.read(4)
		
		CodeAddr = (struct.unpack("<L",CodeAddr))[0]
		NameAddr = (struct.unpack("<L",NameAddr))[0]
		
		q.seek(NameAddr)
		g = 0
		p = "0"
		while p != "FF":
			stringbyte = q.read(1)
			if stringbyte != b'\x00':
				g += 1
			else:
				p = "FF"
			
		q.seek(NameAddr)
		Name = str(q.read(g)).replace("b'","").replace("'","")
		
		CodeAddr = struct.pack(">L",CodeAddr)
		CodeAddr = str(binascii.hexlify(CodeAddr))
		CodeAddr = CodeAddr.replace("b'","0x").replace("'","")
		
		print(Name)
		print(CodeAddr)
		
		k = open("StackTrace_Output.cpp", 'a')
		k.write(str(CodeAddr) + ":\t\t" + str(Name) + "\n")
		i += 1

k.close
	
