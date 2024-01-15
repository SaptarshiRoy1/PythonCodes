import random

a= int(input("Enter the length of the password : "))
b = int(input("Enter the character types (1:Letters 2:Numbers 3:Symbols) : "))
set1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
set2 = "1234567890"
set3 = " !#$%&'()*+,-./:;<=>?@[]^_`{|}~"
password=""
if b == 1:
    for i in range(a):
        password = password+ random.choice(set1)
elif b == 2:
    for i in range(a):
        password = password+ random.choice(set2)
elif b == 3:
    for i in range(a):
        password = password+ random.choice(set3)

print("Your random password is "+password)