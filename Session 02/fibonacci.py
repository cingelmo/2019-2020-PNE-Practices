number = 11
num1 = 0
num2= 1
if number >= 1:
     print(num1, end=' ')
if number >= 2:
    print(num2, end=' ')
if number >= 3:
    for number in range (3, number + 1):
        newnum= num1 + num2
        print(newnum, end=' ')
        num1 = num2
        num2 = newnum
