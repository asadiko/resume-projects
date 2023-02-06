import sys, random, os, time
from sys import exit
print ("welcome to the game!") 
print ("The rules are:\n 1. You have to memorize all the randomly generated sings.\n 2. You have 5 sec to remember.\n 3. Input memorized signes correcly and in correct order.\n 4. Note that you have only 3 attepmts!!")
attempt = input("Do you wanna try? (yes/no): ")
if attempt == "no":
    sys.exit()
wins = 0 
losses = 0
while True:
    print('(%s) Wins, (%s) Losses' % (wins, losses))
    num_charecters = int(input("Please enter the number of charecters: "))
    charecters = "QWERTYUIOPASDFGHJKLZXCVBNMqw>ertyuiopasdfghjklzx<cvbnm123456:7890~-=\][;'/.,']~!@#$%^&*()_+|}{"""
    signs = ""
    for index in range (num_charecters):
      signs = signs + random.choice(charecters)
    print ("Memorize this:  " + signs)
    #timer >>
    minutes = 0
    seconds = 5

    stop_time = '%r:%r' % (minutes, seconds)

    t_minutes = 00
    t_seconds = 00

    while t_seconds <= 60:
        current_time = '%r:%r' % (t_minutes, t_seconds)
        print (current_time)
        time.sleep(1)
        t_seconds+=1
        if current_time == stop_time:
            print ("Time is up!")
            os.system('clear')
            break
        elif t_seconds == 60:
            t_minutes+=1
            t_seconds=0
            break 
    #timer <<
    for i in range (1,4):
     answer = str(input("Enter your answer pleas: "))
     if answer != signs:
        print ("Wrong attempt!")
        losses = losses + 1
     if answer == signs:
        print ("You did a great job!")
        wins = wins + 1
        break 

     
    print ("The answer was " + signs)
    again = input("Do you wanna try again? (yes/no): ")
    if again == "no":
     print('(%s) Wins, (%s) Losses' % (wins, losses))
     sys.exit()
        