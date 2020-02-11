def fibonacci(number):
    num1 = 0
    num2 = 1
    if number < 0:
        return 'Incorrect input'
    elif number == 1:
        return 1
    else:
        count = 0
        sum = 0
        while count < number:
            numth = num1 + num2
            num1 = num2
            num2 = numth
            count += 1
            sum += num1
        return sum
print('Sum of the first 5 terms of the Fibonacci series: ', fibonacci(5))
print('Sum of the first 5 terms of the Fibonacci series: ', fibonacci(10))