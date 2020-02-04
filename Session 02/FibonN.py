def fibonacci (number):
    num1 = 0
    num2= 1
    if number >= 1:
         return num1, end=' '
    if number >= 2:
        return num2, end=' '
    if number >= 3:
        for number in range (3, number + 1):
            newnum= num1 + num2
            return newnum, end=' '
            num1 = num2
            num2 = newnum

print('The 5th Fibonacci term is: ',fibonacci (5))
print('The 10th Fibonacci term is: ',fibonacci (10))
print('The 15th Fibonacci term is: ',fibonacci (15))