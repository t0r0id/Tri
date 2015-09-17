import time
import numpy as np
from Plot import plotTSP
from read_file import read,find_distance,find_segment_length
from knapsack import knpsck_value_mat,knpsck_select_items
from opt_2 import opt2
from greedy_1 import greedy


data=read("Co-ordinates.xlsx")
capacity=24
value_mat=knpsck_value_mat(data,capacity)
selected=knpsck_select_items(value_mat,capacity,data)
points=data[selected][:]

flag=0
while flag==0:
    opt2_result=opt2(points)
    best_distance=opt2_result[0]
    total_time=best_distance/100+points[:,3].sum()
    if total_time<=24:
        flag=1
        route=opt2_result[1]
        print "Happiness_index = " , points[:,2].sum()
        print "Total_time = " , total_time/2
        print "Travelling_time = ", best_distance/200
        plotTSP(route, points,data)
    else:
        capacity=capacity-1
        selected=knpsck_select_items(value_mat,capacity,data)
        points=data[selected][:]
