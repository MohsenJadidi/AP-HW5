import random
import math


# Point in circle?
def IsInCircle(x, y):
    if (x*x + y*y) > 1:
        return False
    else:
        return True


# Estimate PI
def Find():
    err = 0.01
    number_of_points = 0
    number_in = 0
    estimate_pi = 0
    while abs(estimate_pi - math.pi) > err:
        number_of_points += 1
        if IsInCircle(2*random.random() - 1, 2*random.random() - 1):
            number_in += 1
        estimate_pi = 4 * (number_in / number_of_points)

    return estimate_pi, number_of_points


counter = int(input('Please enter an integer:'))

estimatePI = []
numberOfPoints = []
for i in range(counter):
    pi, number = Find()
    estimatePI.append(pi)
    numberOfPoints.append(number)

print('Average Number of Points : %8.5f' % (sum(numberOfPoints)/len(numberOfPoints)))
print('Average Estimate PI : ', sum(estimatePI)/len(estimatePI))

