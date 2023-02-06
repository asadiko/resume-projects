import numpy as np
import os
#Introduction
matrix = np.array([[int(input('First matrix:\n1st number of 1st raw: ')), int(input('2nd number of 1st raw: ')), int(input('3rd number of 1st raw: '))], [int(input('1st number of 2nd raw: ')), int(input('2nd number of 2nd raw: ')), int(input('3rd number of 2nd raw: '))], [int(input('1st number of 3rd raw: ')), int(input('2nd number of 3rd raw: ')), int(input('3rd number of 3rd raw: '))]])
matrix1 = np.array([[int(input('Second matrix:\n1st number of 1st raw: ')), int(input('2nd number of 1st raw: ')), int(input('3rd number of 1st raw: '))], [int(input('1st number of 2nd raw: ')), int(input('2nd number of 2nd raw: ')), int(input('3rd number of 2nd raw: '))], [int(input('1st number of 3rd raw: ')), int(input('2nd number of 3rd raw: ')), int(input('3rd number of 3rd raw: '))]])
os.system('clear')
print(matrix)
print('\nWith matrices you can do:\n 1.Find the sum of matrices.\n 2.Substract matrices  \n 3.Multiply matrices.\n 4.Find the determinant of matrices.\n ')
choice = int(input('Your input: '))
#Calculation part
if choice == 1: 
 def sum_matrix():
    first_raw = (matrix[0, 0] + matrix1[ 0, 0], matrix[ 0, 1] + 
                 matrix1[ 0, 1], matrix[ 0, 2] + matrix1[ 0, 2])
    second_raw = (matrix[ 1, 0] + matrix1[ 1, 0],  matrix[ 1, 1] +
                  matrix1[ 1, 1], matrix[ 1, 2] + matrix1[ 1, 2])
    third_raw = (matrix[ 2, 0] + matrix1[ 2, 0],  matrix[2, 1] + 
                 matrix1[ 2, 1], matrix[ 2, 2] + matrix1[ 2, 2])
    summe = np.concatenate([first_raw, second_raw, third_raw])
    newarrr = np.array_split(summe, 3)
    return newarrr
 summ = sum_matrix()
 print("\n\nThe answer is: ")
 print(summ[0])
 print(summ[1])
 print(summ[2])
#minus
if choice == 2:
 def minus_matrix():
    first_raw = (matrix[0, 0] - matrix1[ 0, 0], matrix[ 0, 1] - 
                 matrix1[ 0, 1], matrix[ 0, 2] - matrix1[ 0, 2])
    second_raw = (matrix[ 1, 0] - matrix1[ 1, 0],  matrix[ 1, 1] - 
                  matrix1[ 1, 1], matrix[ 1, 2] - matrix1[ 1, 2])
    third_raw = (matrix[ 2, 0] - matrix1[ 2, 0],  matrix[ 2, 1] - 
                 matrix1[ 2, 1], matrix[ 2, 2] - matrix1[ 2, 2])
    minuse = np.concatenate([first_raw, second_raw, third_raw])
    newarr = np.array_split(minuse, 3)
    return newarr
 minus = minus_matrix()
 print("\n\nThe answer is: ")
 print(minus[0])
 print(minus[1])
 print(minus[2])
#multiply
if choice == 3:
 def multiply_matrix():
    m3 = np.dot(matrix, matrix1)
    return m3
 mult = multiply_matrix()
 print("\n\nThe answer is: " + str(mult))
#determinant
if choice == 4:
 det = np.linalg.det(matrix)
 det1 = np.linalg.det(matrix1)
 print("\n\nThe answer of first det is: " + str(det))
 print("\n\nThe answer of second det is: " + str(det))
   









