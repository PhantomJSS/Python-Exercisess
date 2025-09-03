## Exercise #1

## print("Hello World " * 4)



## Exercise #2

## favfruit = "Mango"
## print(f'Your favourite fruit is: {favfruit} ' * 50)

## favcolour = input("Please enter what is your favourite colour: ")
##print(f'Your favourite colour is: {favcolour} ' * 50)



## Exercise #3

##num = int(input("Please enter in a number of your choice: "))
##if num % 2 == 0:
##    print(f'Your number {num} is even')
##else:
##    print(f'Your number {num} is odd')

##age = int(input("Please enter in your age: "))
##if age >= 18:
##    print("You are an adult")
##else:
##    print("You are a minor")

##num = int(input("Please enter in a nuber of your choice: "))
##if num >= 0:
##    print("Your number is positive")
##else:
##    print("Your number is negative")



## Exercise #4

##count = 0
##sent = input("Please enter in a string of your choice: ").lower()
##for character in sent:
##    if character in "aeiou":
##        count +=1
##print(f'The total number of vowels in your sentence is {count}')



## Exercise #5

##sent = input("Please enter in a sentence of your choice: ").lower()
##for character in sent:
##    if character in "aeiou":
##        sent = sent.replace(character, "*")
##print(f"Your updated sentence is {sent}")

##for number in range(1, 11):
##    print(number)

##num = int(input("Please enter in a number of your choice: "))
##for number in range (1, 11):
##    print(num * number)



## Exercise #6

##sent = input("Please enter in a sentence of your choice: ").lower()
##for character in sent:
##    if character in "aeiou":
##        sent = sent.replace(character, "")
##print(f'Your updated sentence is: {sent}')



## Exercise #7

##word = input("Please enter in a word of your choice: ").lower()
##reverse = ""
##for character in word:
##    reverse = character + reverse
##if reverse == word:
##    print(f'Your word {word} is a palindrome')
##else:
##    print(f'Your word {word} is not a palindrome')

##count = 0
##words = input("Please enter in a list of words of your choice: ").lower()
##list = words.split()
##for string in list:
##    if string[0] in "aeiou":
##        count +=1
##print(f'You entered in a total of {count} words that start with a vowel')



## Exercise #8

##word = input("Please enter in a word of your choice: ")
##print(word.lower())
##print(word.upper())

##word = input("Please enter in a word of your choice: ")
##reverse = ""
##for character in word:
##    reverse = character + reverse
##print(f'Your reversed word is {reverse}')




## Exercise #9

##groclist = ["apple", "banana", "bread", "eggs", "milk", "cream", "sugar", "salt", "biscuits", "chocolate", "chips"]
##favsnack = input("Please enter in your favourite snack from the list: ").lower()
##if favsnack in groclist:
##    print(f"Your favourite snack {favsnack} is in the list")
##else:
##    print(f'Your favourite snack {favsnack} is not in the list')




## Exercise #10

##names = input("Please enter in a list of names of your choice: ").split()
##names.sort()
##print(names)