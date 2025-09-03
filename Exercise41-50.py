## Exercise 41

##import base64
##msg = input('Please enter in a message of your choice: ')
##base64_bytes = msg.encode('utf-8')
##msg_byte = base64.b64decode(base64_bytes)
##print(f'Your decoded message is the following: {msg_byte.decode('utf-8')}')



## Exercise 42

##import hashlib
##file = input('Please enter in the filename of your choice: ')
##with open(file, 'rb') as f:
##    content = f.read()
##    md5 = hashlib.md5()
##    md5.update(content)
##    checksum = md5.hexdigest()
##    f.close()
##print(f'The MD5 Checksum for the file is {checksum}')



## Exercise 43

##import hashlib
##file = input('Please enter in the filename of your choice: ')
##with open(file, 'rb') as f:
##    content = f.read()
##    sha256 = hashlib.sha256()
##    sha256.update(content)
##    checksum = sha256.hexdigest()
##    f.close()
##print(f'The SHA256 Checksum for the file is {checksum}')



## Exercise 44

##import string
##msg = input('Please enter in a sentence of your choice: ')
##newmsg = []
##for char in msg:
##    asciic = ord(char)
##    newmsg.append(asciic)
##print(f'Your message in ASCII representation is: {newmsg}')



## Exercise 45

##import turtle
##myturt = turtle.Turtle()
##for i in range(4):
##    myturt.forward(100)
##    myturt.right(90)
##myturt.hideturtle()
##turtle.done()



## Exercise 46

import requests
from bs4 import BeautifulSoup
profile = input('Please enter in the username of your choice: ')
urls = {}


## Exercise 47

## Exercise 48

## Exercise 49

## Exercise 50