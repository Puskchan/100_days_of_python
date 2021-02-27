import random
import string
# print("Welcome to password generator!")
a = int(input("How long do you want the password?: \n"))
b = int(input("How many special characters?: \n"))
c = int(input("How many numbers?: \n"))

long = ""
for i in range(0,(a-(b+c))):
    k = random.choice(string.ascii_letters)
    long+=k

spchar = ""
for i in range(0,b):
    k = random.choice(string.punctuation)
    spchar += k

no = ""
for i in range(0,c):
    k = random.choice(string.digits)
    no+=k

passwd = (long + spchar + no)

m = random.sample(passwd,a)

s = ""
for i in m:
    s += i

print(s)
