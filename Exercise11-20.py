## Exercise #11

##words = input("Please enter in a list of words of your choice: ")
##list = words.split()
##longest = list[0]
##for string in list:
##    if len(longest) < len(string):
##        longest = string
##print(f'The longest word in your list is {longest}')



## Exercise #12

##import random
##emojis = ['❌', '🙌', '🔒', '😝', '🙈']
##word = input('Please enter in a word of your choice: ').lower()
##for character in word:
##    if character in 'aeiou':
##        word = word.replace(character, random.choice(emojis))
##print(f'Your new word with emojis is {word}')



## Exercise #13

##validname = "admin"
##validpass = "admin"
##user = input("Please enter in your username: ")
##password = input("Please enter in your password: ")
##if user == validname and password == validpass:
##    print('Your username and password are too easy to phish, use new credentials')
##else:
##    print('You pass the phisihing test, your credentials are safe')



## Exercise #16

##phishing = ['evil.com', 'phishing101.ca', 'hacker123.com']
##url = input('Please enter in the suspected URL: ').split("//")[-1].split("/")[0]
##if url in phishing:
##    print(f'The provided URL of {url} is a known phishing webpage')
##else:
##    print(f'The provided URL of {url} is a safe webpage')



## Exercise #17

##sales = {"Sales": 18000, "Marketing": 20000, "Security":10000, "R&D":19000}
##highest = max(sales, key=sales.get)
##print(highest)



## Exercise #18

##import random
##import string
##length = 12
##password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
##print(f'Your generated password is: {password}')



## Exercise #19

##import random
##num = random.randint(1, 10)
##guess = int(input('Please enter in your guess for the random number: '))
##while guess != num:
##    if guess > num:
##        print('Your guess is too high, please try again: ')
##    else:
##        print('Your guess is too low, please try again: ')
##    guess = int(input('Please enter in your guess for the random number: '))
##print(f'You have guessed correctly, the number was {num}')


    
## Exercise #20

##import re
##password = input('Please enter in a password of your choice: ')
##if len(password) < 8:
##    print('Your password is too short')
##elif not re.search("[A-Z]", password):
##    print('Your password needs to have an uppercase letter')
##elif not re.search("[a-z]", password):
##    print('Your password needs to have a lowercase letter')
##elif not re.search("[0-9]", password):
##    print('Your password must have a number')
##else:
##    print('Your password satisfies the conditions and is strong')