import sys, time, os
print('HEEEYYYYY!!\nThis in Guess game , rules are:\n 1. You will be shown some variables attached to each other.\n 2. After a while they will be deleted.\n 3. You have to guess in correct order and matching.\n 4. You have 5 seconds to memorize.')
gameset = {'Asad', 'Murad', 'Shatsi', 'Asilbek', 'Saidbek', 'Timur'}
listmaker = list(gameset)
Asad = "Asad was born on 9th of June"
Murad = 'Murad was born on 19th of April'
Shatsi = 'Shatsi was born on 30th of OCtober'
Asilbek = 'Asilbek was born on 19th of September'
Saidbek = 'Saidbek was born on 18th of September'
Timur = 'Timur was born on н19th of July'
gamersdesicion = input('\nDo you want to try? (yes/no): ')
if gamersdesicion == 'no':
    os.system('clear')
    sys.exit("I thought you'd like to attempt(\n")
else:
    print('Invalid input!')
os.system('clear')
print("Great!\nLet's start our game!")
wins = 0
losses = 0
while True:
    print('  %s Wins, %s Losses' %(wins, losses) + '                <- This is our counter\n')
    def countdown(t):
    
     while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    t = 5
    countdown(int(t))
    os.system('clear')
    #timer <<
    print('\nThese are the birhdays of students, remeber it: ')
    print("""  Asad = '9th of June'
  Murad = '19th of April'
  Shatsi = '30th of October'
  Asilbek = '18th of September'
  Saidbek = '19th of September'
  Timur = '19th of July'\n""""")
    #timer >
    def countdown(t):

     while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    t = 5
    countdown(int(t))
    #timer <<
    os.system('clear')
    print('Now you have to match the birthdays: ')
    print(gameset)
    print('\nPlease input your answers: ' + '                               <-   Answer should be like: Mikle was born on 15th of July ')
    asad = input('1. Input the name and the date:  ')
    murad = input('2. Input the name and the date:  ')
    shatsi = input('3. Input the name and the date:  ')
    asilbek = input('4. Input the name and the date:  ')
    saidbek = input('5. Input the name and the date:  ')
    timur = input('6. Input the name and the date:  ')
    answers = input('\nReady to see the answers?  (press Enter)')
    if answers == '':
        os.system('clear')
    if asad == 'Asad was born on 9th of June':
        print('\n1. Valid input')
        wins += 1
    else:
        print('\n1. Invalid input' + '       -> ' + Asad)
        losses += 1
    if murad == 'Murad was born on 19th of April':
       print('2. Valid input')
       wins += 1
    else:
        print('2. Invalid input' + '       -> ' + Murad)
        losses += 1
    if shatsi == 'Shatsi was born on 30th of October':
       print('3. Valid input')
       wins += 1
    else:
        print('3. Invalid input' + '       -> ' + Shatsi)
        losses += 1
    if asilbek == 'Asilbek was born on 18th of September':
       print('4. Valid input')
       wins += 1
    else:
        print('4. Invalid input' + '       -> ' + Asilbek)
        losses += 1
    if saidbek == 'Saidbek was born on 19th of September':
       print('5. Valid input')
       wins += 1
    else:
        print('5. Invalid input' + '       -> ' + Saidbek)
        losses += 1
    if timur == 'Timur was born on 19th of July':
       print('6. Valid input')
       wins += 1
    else:
        print('6. Invalid input' + '       -> ' + Timur)
        losses += 1
    print('\nYour scores are:      %s Wins, %s Losses' % (wins, losses))
    if wins > losses:
        print('You have great memory!')
    if losses > wins:
        print('Train your memory!')
    if wins == losses:
        print('You can do better!')
    attempt = input('\nWanna reattempt?  (yes/no)   ')
    if attempt == 'no':
        os.system('clear')
        sys.exit('Will be waiting for your next try)\n ')
    elif attempt == 'yes':
        continue
    else:
        print('Invalid input')