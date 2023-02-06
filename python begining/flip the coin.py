import random
import sys 
print("\nWelcome to the Coin Flip", end='')
print("!\n")
while True:
 coin = input('Do you want to flip the coin? (yes/no): ')
 for coin in ('yes', 'no'):
    if coin == 'yes':
        for i in range (random.randint(0,4)):
            if i == 0:
                print("Tail")
                break
            if i == 1:
                print("Head")
                break
            if i == 2:
                print("Tail")
                break
            if i == 3: 
                print("Head")
                break
    if coin == 'no':
        sys.exit()
 else:
     print('Invalid input')
    