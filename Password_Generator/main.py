import random
import string

print('\n')
print("Enter the desired length of password: \n")

pass_length = input()
pass_length = int(pass_length)

ucase_length = int(pass_length/4)
char_length  = int(pass_length/4)
digit_length = int(pass_length/4)
lcase_length = pass_length - digit_length - ucase_length - char_length

#lower case letters
lcase = random.sample(string.ascii_lowercase, lcase_length)

#upper case letters
ucase = random.sample(string.ascii_uppercase, ucase_length)

#digits from 0 to 9
digits = []
for i in range(digit_length):
    number = str(random.randint(0,9))
    digits.append(number)

#selected characters
characters = []
for i in range(char_length):
    character = random.choice("~!@#$%^&*()_+=-")
    characters.append(character)

password = lcase + ucase + digits + characters

random.shuffle(password) #shuffle all the characters of the password

print('\n')
print("Your password is : ")
print("".join(password))
print('\n')
