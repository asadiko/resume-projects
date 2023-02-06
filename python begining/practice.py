birthday = {'Asad': 'June 9th in 2004', 'Murad': 'April 19th in 2003', 'Asilbek': 'September 19th in 2003'}
while True:
    name = input('Enter name (blank to quit): ')
    if name == '':
        break 
    if name in birthday:
        print(name + "'s birthday is on " + birthday[name])
    else:
        print("I don't have any data about " + name + '.')
        bday = input('Enter birthday and year: ')
        birthday[name] = bday
        print('Birthdays data updated.')
        break 