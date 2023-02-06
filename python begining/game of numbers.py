import random 
pc_number = random.randint(1,20)
print ("My number is between 1 and 20.\nYou have 3 chances to find this number.")
for guess_taken in range(1, 4):
  print ("Guess the number:")
  guess = int(input())
  if guess < pc_number:
    print ("It's not enough!")
  elif guess > pc_number:
    print ("It's too much!")
  else:
   if  guess == pc_number:
    print ("You guessed the number from" + " "+ str(guess_taken) + " " + "time!")
    break 
else:
   print("Hey dude your chances are gone because it is already " + str(guess_taken) + "rd" + " " + "time!")
   print ("The number I have guessed was " + str(pc_number) + ")")
