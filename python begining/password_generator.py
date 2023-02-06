import random 
print ("IT'S A NEW NUMBERS, LETTERS, CHARECTERS GENERATER!")
num_charecters = int(input("Please enter the number of charecters: "))
charecters = "QWERTYUIOPASDFGHJKLZXCVBNMqw>ertyuiopasdfghjklzx<cvbnm123456:7890~-=\][;'/.,']~!@#$%^&*()_+|}{"""
password = ""
for index in range (num_charecters):
    password = password + random.choice(charecters)
print ("Password generated: " + password)