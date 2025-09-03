## Exercise 31

##words = input('Please input in a list of words of your choice: ').split()
##newlist = []
##for string in words:
##    new = ""
##    reverse = string[::-1]
##    for character in reverse:
##        if character not in "aeiou":
##            new += "!"
##        else:
##            new += character
##    newlist.append(new)
##print(f'Your updated list is: {newlist}')



## Exercise 32

##import os
##host = input('Please enter the hostname that you would like to check: ')
##response = os.system("ping -c 1" +host)
##if response == 0:
##    print(f'The host name {host} is not reachable')
##else:
##    print(f'The host name {host} is reachable')



## Exercise 33

##words = input('Please enter in a list of words of your choice: ').upper().split()
##newlist = []
##for string in words:
##    reverse = string[::-1]
##    newlist.append(reverse)
##print(f'Your updated list is: {newlist}')



## Exercise 34

##import requests
##url = input('Please enter in a URL of your choice: ')
##filename = input('Pleae enter in the filename: ')
##response = requests.get(url)
##with open(filename, 'w') as file:
##    file.write(response.text)
##print(f'The source code for the given URL has been saved to the {filename} file')


## Exercise 35

##import random
##moves = ['rock', 'paper', 'scissors']
##player = input('Please pick a move to throw (Rock, Paper, Scissors): ').lower()
##comp = random.choice(moves)
##if player == comp:
##    print(f'Both players threw {comp}, the match is a draw')
##elif (player == "rock" and comp == "scissors" or \
##      player == "paper" and comp == "rock" or \
##      player == "scissors" and comp == "paper"):
##    print(f'The computer threw {comp}, you win the match')
##else:
##    print(f'The computer threw {comp}, you lose the match')


## Exercise 36

##name = input('Please enter in your name: ')
##print(f'Nice to meet you *{name}*')



## Exercise 37

##key = 3
##word = input('Please enter in any sentence of your choice: ')
##cipher = ""
##for character in word:
##    if character.isalpha():
##        shift = key % 26
##        start = ord('a') if character.islower() else ord('A')
##        cipher += chr((ord(character) - start + shift) % 26 + start)
##    else:
##        cipher += character
##print(f'Your transformed sentence in ciphertext is {cipher}')



## Exercise 38

##import whois
##domain = input('Please enter in the domain name of your choice: ')
##info = whois.whois(domain)
##print(f'Registrar: {info.registrar}')
##print(f'Creation Date: {info.creation_date}')
##print(f'Expiration Date: {info.expiration_date}')
##print(f'Name Servers: {info.name_servers}')



## Exercise 39

##import hashlib
##msg = input('Please enter in a message of your choice: ')
##md5 = hashlib.md5()
##md5.update(msg.encode())
##hash = md5.hexdigest
##print(f'The hash for the inputted message is: {hash}')



## Exercise 40

##import base64
##msg = input('Please enter in a message of your choice: ')
##encoded = msg.encode('utf-8')
##bytes = base64.b64encode(encoded)
##decoded = bytes.decode('utf-8')
##print(f'The Base64 encoded version for the inputted message is: {decoded}')
