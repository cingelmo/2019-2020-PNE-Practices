user_input = input('Introduce the sequence: ')
counterA = 0
counterC = 0
counterT = 0
counterG = 0
i = 0
while i < len(user_input):
    if user_input[i] == 'A':
        counterA = counterA + 1
    elif user_input[i] == 'C':
        counterC = counterC + 1
    elif user_input[i] == 'T':
        counterT = counterT + 1
    elif user_input[i] == 'G':
        counterG = counterG + 1
    i += 1

print('Total length: ', len(user_input))
print(' A: ', counterA, '\n C: ', counterC, '\n T: ', counterT, '\n G: ', counterG)

