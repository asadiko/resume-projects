l1 = [2,4,3]
l2 = [5,6,4]

l1.reverse()
l2.reverse()
num1 = ''.join(map(str, l1))
num1 = int(num1)
num2 = ''.join(map(str, l2))
num2 = int(num2)

summ = num1 + num2
summ = str(summ)
done = "".join(map(str, summ))
done = list(done)
done.reverse()
print(done)
