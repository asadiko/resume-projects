#Celsius to Fahrenheit
print('Converter from Celsius to Fahrenheit!')

Celsius = float(input('Please input a temperature: '))
#Converting formula
def convert():
    Fahrenheit = (Celsius * 1.8) + 32
    return Fahrenheit
print('Here is the answer: ', convert())