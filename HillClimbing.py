
import math
import random

def f1(x,y):
    if(x < 0 or x > 10):
        return none
    if(y < 0 or y > 10):
        return none
    return math.sin(x/2)+math.cos(2*y)

def f2(x,y):
    if(x < 0 or x > 10):
        return none
    if(y < 0 or y > 10):
        return none
    return -abs(x-2)-abs(y/2+1) + 3

def findNeighbors(x,y,StepSize,function,max0):
    neighbors = [(x-StepSize,y),(x-StepSize,y-StepSize),(x-StepSize,y+StepSize),(x+StepSize,y),(x+StepSize,y-StepSize),(x+StepSize,y+StepSize),(x,y+StepSize),(x,y-StepSize)]
    for (x_new,y_new) in neighbors:
        if x_new > 0 and x_new < 10 and y_new > 0 and y_new < 10 and function(x_new,y_new) > max0:
            max0 = function(x_new,y_new)
            (x,y) = (x_new,y_new)
    return x,y,max0

def HillClimbing(function):
    for StepSize in [0.01,0.05,0.1,0.2]:
        mean = 0
        average = 0
        sq_sum = 0
        sq_ave = 0
        summation = 0
        for i in range(100):
            index = 0
            (x0,y0) = (random.uniform(0,10),random.uniform(0,10))
            max0 = function(x0,y0)
            (x_new,y_new,max_new) = findNeighbors(x0,y0,StepSize,function,max0)
            while max0 != max_new:
                max0 = max_new
                x0 = x_new
                y0 = y_new
                (x_new,y_new,max_new) = findNeighbors(x0,y0,StepSize,function,max0)
                index += 1
            average = average + max0
            summation = summation+index
            sq_ave = sq_ave + pow(max0,2)
            sq_sum = sq_sum + pow(index,2)
        result_mean = average/100
        result_std = math.sqrt((100*sq_ave-pow(average,2))/(100*99))
        conv_mean = summation/100
        conv_std = math.sqrt((100*sq_sum-pow(summation,2))/(100*99))
        print("steps:",index,"stepsize",StepSize,"result_mean:", result_mean,"result_std:",result_std,"conv_mean:",conv_mean,"conv_std: ",conv_std)

print("Result for function 1: ")
HillClimbing(f1)
print("-------")
print("Result for function 2: ")
HillClimbing(f2)
