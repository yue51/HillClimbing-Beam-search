import math
import numpy as np
import random
from operator import itemgetter

def f1(x,y):
    return math.sin(x/2)+math.cos(2*y)
def f2(x,y):
    return -abs(x-2)-abs(y/2+1)+3

def neighbours(record,StepSize,function,beam_width):
    #neighbours=np.zeros((beam_width*8,3))
    neighbours=[(0,0,0)]*(8*beam_width)
    i=0
    for (x,y,value) in record:
        neighbours[8*i]=(x-StepSize,y-StepSize,function(x-StepSize,y-StepSize))
        neighbours[8*i+1]=(x-StepSize,y,function(x-StepSize,y))
        neighbours[8*i+2]=(x-StepSize,y+StepSize,function(x-StepSize,y+StepSize))
        neighbours[8*i+3]=(x,y-StepSize,function(x,y-StepSize))
        neighbours[8*i+4]=(x,y+StepSize,function(x,y+StepSize))
        neighbours[8*i+5]=(x+StepSize,y-StepSize,function(x+StepSize,y-StepSize))
        neighbours[8*i+6]=(x+StepSize,y,function(x+StepSize,y))
        neighbours[8*i+7]=(x+StepSize,y+StepSize,function(x+StepSize,y+StepSize))
        i=i+1
    j=0
    for (x,y,value) in neighbours:
        if x<0 or 10<x or y<0 or 10<y:
            neighbours[j]=(0,0,-11)
        j=j+1
    return neighbours 
    
def BeamSearch(function,StepSize):
    for beam_width in [2,4,8,16]:
        summation=0
        mean=0
        sq_mean=0
        sq_sum=0
        for k in range(100):
            index=1;
            record=[(0,0,0)]*beam_width 
            for j in range(beam_width):
                record[j]=[(random.uniform(0,10),random.uniform(0,10),0)]
                [(x,y,z)]=record[j]
                record[j]=(x,y,function(x,y))

            record=sorted(record, key=itemgetter(2), reverse=True)
            (x_low,y_low,lowest_value)=record[beam_width-1]
            neighbor_temp = neighbours(record,StepSize,function,beam_width)
            neighbours_ini=sorted(neighbor_temp, key=itemgetter(2), reverse=True);
            (x_high,y_high,highest_value)=neighbours_ini[0]

            while (highest_value > lowest_value):
                temp=record+neighbours_ini
                temp=sorted(temp, key=itemgetter(2), reverse=True)
                for k in range(0,beam_width):
                    (x1,y1,value1)=temp[k]
                    record[k]=(x1,y1,value1)
                (x_low,y_low,lowest_value)=record[beam_width-1]
                neighbor_temp = neighbours(record,StepSize,function,beam_width)
                neighbours_ini=sorted(neighbor_temp, key=itemgetter(2), reverse=True);
                (x_high,y_high,highest_value)=neighbours_ini[0]
                index=index+1

            (x2,y2,value2)=record[0]
            summation += index
            mean+=value2
            sq_mean+=pow(value2,2)
            sq_sum +=pow(index,2) 

        conv_mean=summation/100
        result_mean=mean/100
        result_std=math.sqrt((100*sq_mean-pow(mean,2))/(100*99))
        conv_std=math.sqrt((100*sq_sum-pow(summation,2))/(100*99))
        print("Step:",summation,"Beam Width:",beam_width,"Convergence mean:",conv_mean,"Result mean:",result_mean,"Convergence standard deviation:",conv_std,"Result standard deviation:", result_std)
 

print("Result for function 1")
BeamSearch(f1,0.01)
print("-----------")
print("Result for function 2")
BeamSearch(f2,0.01)



