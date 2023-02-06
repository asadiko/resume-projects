#Write an algorithm to find the largest among three different numbers entered by the user. 
#(use any programming language)
print("Let's find the largest among three numbers!")
 
number_a = float(input('Please enter first number: '))
number_b = float(input('Please enter second number: '))
number_c = float(input('Please enter third number: '))

#find the gratest number
if number_a > number_b and number_a > number_c:
    largest = number_a
if number_b > number_a and number_b > number_c:
    largest = number_b
if number_c > number_a and number_c > number_b:
    largest = number_c

print('The largest number is first: ', largest)

