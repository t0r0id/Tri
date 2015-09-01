import time
import numpy as np
from Plot import plotTSP
from read_file import read,find_distance,find_segment_length

def next_point(not_visited,dis,points):
    mini=9999 
    for i in range (points.shape[0]):
        if (not_visited[i]) & (dis[i]>0) & (dis[i]<mini):
            mini=dis[i]
            nxt=i
    return nxt

def greedy(points):
    distance=find_distance(points)
    route = np.empty(0,dtype=int)
    not_visited=np.ones(points.shape[0],dtype=bool)
    not_visited[0]=0
    route=np.append(route,0)
    nxt=0
    for i in range(points.shape[0]-1):
        dis=distance[nxt][:]
        nxt=next_point(not_visited,dis,points)
        route=np.append(route,nxt)
        not_visited[nxt]=0
    route=np.append(route,0)
    best_distance=np.sum(find_segment_length(route,distance))
    return (best_distance,route)





    
