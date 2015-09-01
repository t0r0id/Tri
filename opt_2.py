import time
import numpy as np
from Plot import plotTSP
from read_file import read,find_distance,find_segment_length
from knapsack import knpsck

def find_neighbour(route,a,b):
    t1=min(a,b)
    t2=max(a,b)
    new_route=np.zeros(route.shape[0],dtype=int)
    for i in range(0,t1):
        new_route[i]=route[i]
    for i in range (t1,t2+1):
        new_route[i]=route[t2-i+t1]
    for i in range(t2+1,route.shape[0]):
        new_route[i]=route[i]
    return new_route

def opt2(points):
    distance=find_distance(points)
    route=np.arange(distance.shape[0])
    route=np.append(route,0)
    segments=find_segment_length(route,distance)
    flag=0
    while flag ==0:
        best_distance= np.sum(segments)
        for i in range(1,route.shape[0]-2):
            for j in range (i+1,route.shape[0]-1):
                new_route=find_neighbour(route,i,j)
                new_distance=np.sum(find_segment_length(new_route,distance))
                if new_distance<best_distance:
                    best_distance=new_distance
                    route=new_route
                    i=1
                    j=1
        flag=1
    return (best_distance,route)



