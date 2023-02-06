import sys, os
students = []
while True:
    print ("Enter names of all students " + str(len(students) + 1) +" (Or enter nothing to stop.):" )
    names = input()
    if names == '':
        os.system('clear')
        break 
    students = students + [names]
print("The students are:")
for name in students:
    print (' ' + name)
print ("If you forgot to add someone eneter here.")
for i in range (0, int(input("How many students did you forget to enter: "))):
 students.append(input("Enter names of all students " + str(len(students) + 1) + ":"))
os.system('clear')
print ("The students are:")
for name in students:
    print (' ' + name)
delete = input("If you added wrong student you can delete.\n Do you want to delete? (yes/no):  ")
if delete == 'no':
    sys.exit()
for ochir in range (0, int(input("Enter how many students would you like to delete: "))):
 ochir = students
 ochir.remove(input("Enter name: "))
os.system('clear')
print ("The students are:")
for name in students:
 print (' ' + name)
 



    