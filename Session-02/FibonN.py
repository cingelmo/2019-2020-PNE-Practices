def fibonacci(number):
    a = 0
    b = 1
    if number < 0:
        return 'Incorrect input'
    elif number == 0 :
        return a
    elif number == 1 :
        return b
    else:
        for i in range (2,number):
            c = a + b
            a = b
            b = c
        return b


print('The 5th Fibonacci term is: ',fibonacci(5))
print('The 10th Fibonacci term is: ',fibonacci(10))
print('The 15th Fibonacci term is: ',fibonacci(15))