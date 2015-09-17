import time
import numpy as np
from Plot import plotTSP
from read_file import read,find_distance,find_segment_length
from knapsack import knpsck_value_mat,knpsck_select_items
from opt_2 import opt2
from greedy_1 import greedy

# select points which maximizes happiness index for maximun capacity using knapsack
# find travel time using opt2
# if travel time + time to visit places > maximum hours in hand (24)
# decrese capacity by 1 and repeat

data=read("data.xlsx")
# column    data
#   0      x_cordinate
#   1      y_cordinate
#   2      happiness index
#   3      time spent at that place(hours)

capacity=24   # number of hours for a day=capacity
value_mat=knpsck_value_mat(data,capacity) # value matrix using dynamic algorithm
selected=knpsck_select_items(value_mat,capacity,data)
points=data[selected][:]

flag=0
while flag==0:
    opt2_result=opt2(points)
    best_distance=opt2_result[0]
    total_time=best_distance/50+points[:,3].sum() # speed is 50 km/hr
    if total_time<=24:
        flag=1
        route=opt2_result[1]
        print "Happiness_index = " , points[:,2].sum()
        print "Total_time = " , total_time
        print "Travelling_time = ", best_distance/50
        plotTSP(route, points,data)
    else:
        capacity=capacity-1
        selected=knpsck_select_items(value_mat,capacity,data)
        points=data[selected][:]
