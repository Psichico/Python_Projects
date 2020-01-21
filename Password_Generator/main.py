import random
import string

print("Enter the desired length of password: \n")
pass_length = input()
pass_length = int(pass_length)

lcase_length = int(pass_length/4)
ucase_length = int(pass_length/4)
char_length  = int(pass_length/4)

remaining = pass_length - lcase_length - ucase_length - char_length


lcase = random.sample(string.ascii_lowercase, lcase_length)
ucase = random.sample(string.ascii_uppercase, ucase_length)

#digits = random.sample(range(10000000), remaining)
digits = []
for i in range(remaining):
    number = str(random.randint(0,9))
    digits.append(number)

characters = []
for i in range(char_length):
    character = random.choice("~!@#$%^&*()_+=-")
    characters.append(character)

#print(characters)


#print(type(digits))
#print("\n")
#print(type(lcase))
#print("\n")
#print(type(ucase))
#print("\n")

password = lcase + ucase + digits + characters

random.shuffle(password)

print("Your password is : ")
print("".join(password))
print('\n')


