filename= input('Enter the name of your file:')
with open(filename,'r') as file:
    counterA = 0
    counterC = 0
    counterT = 0
    counterG = 0
    i = 0
    for line in file:
        for character in line:
            if character == 'A':
                counterA += 1
            elif character == 'C':
                counterC += 1
            elif character == 'T':
                counterT += 1
            elif character == 'G':
                counterG += 1
            i += 1

print('Total length: ', counterA + counterC + counterG + counterT)
print(' A: ', counterA, '\n C: ', counterC, '\n T: ', counterT, '\n G: ', counterG)