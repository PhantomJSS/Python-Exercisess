## Exercise 21

##tuple = (1, 5, 3, 4, 5)
##print(tuple.index(5))
##print(len(tuple))
##print(min(tuple))
##print(max(tuple))
##print(sorted(tuple))



## Exercise 22

##import os
##print(f'The current working directory is: {os.getcwd()}')
##print(f'The list of files in the directory is: {os.listdir()}')
##os.mkdir("Hello")
##os.rmdir("Hello")
##file = open("My name is", "w")
##file.close()
##os.rename("My name is", "Hello")
##if os.path.isdir("Test"):
##    print('The requested directory exists')
##else:
##    print('The requested directory does not exist')



## Exercise 23

##list = []
##while True:
##    print('Your Current List:')
##    for item in list:
##        print("- " + item)
##    print("1 - Add an Item")
##    print("2 - Remove an Item")
##    print("3 - Quit")
##    choice = int(input('Please type in one of the above options: '))
##    if choice == 1:
##        add = input('Please enter in an item of your choice: ')
##        list.append(add)
##    elif choice == 2:
##        remove = input('Please enter in an item you would like to remove: ')
##        list.remove(remove)
##    elif choice == 3:
##        break
##    else:
##        print('Please select a valid option')



## Exercise 24

##def vowel_count(sentence):
##    count = 0
##    for character in sentence:
##        if character in "aeiou":
##            count +=1
##    return count
##word = input('Please enter in a sentence of your choice: ').lower()
##counter = vowel_count(word)
##print(f'The total number of vowels in your sentence is: {counter}')



## Exercise 25

##import random
##import string
##phrase = input('Please enter in a passphrase of your choice: ').strip()
##password = "".join(random.choices(phrase + string.ascii_letters + string.digits + string.punctuation, k=15))
##print(f'Your generated password is {password}')



## Exercise 26

##import requests
##url = input('Please enter in the URL of your choice: ')
##response = requests.get(url)
##print(f'Your URL returned the following response: {response.status_code}')



## Exercise 27

##import random
##emojis = ['❌', '🙌', '🔒', '😝', '🙈']
##newlist = []
##words = input('Please enter in a list of words of your choosing: ').split()
##for string in words:
##    new = ""
##    for character in string:
##        if character in "aeiou":
##            new += random.choice(emojis)
##        else:
##            new += character
##    newlist.append(new)
##print(f'Your updated list is: {newlist}')



## Exercise 28

##import requests
##from bs4 import BeautifulSoup
##url = input('Please enter in a URL of your choice: ')
##response = requests.get(url)
##if response.status_code == 200:
##    soup = BeautifulSoup(response.text, 'html.parser')
##    print(soup.prettify())



## Exercise 29



## Exercise 30

