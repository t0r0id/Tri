import numpy as np

def knpsck(points,capacity):
    value_mat=np.zeros((capacity+1,points.shape[0]+1), dtype=np.int)
    for item in range (points.shape[0]):
        for weight in range(1,int(points[item][3])):
            value_mat[weight][item+1]= value_mat[weight][item]
        for weight in range(int(points[item][3]),capacity+1):
            value_mat[weight][item+1]= max(points[item][2]+value_mat[weight-points[item][3]][item],value_mat[weight][item])
    col = np.argmax(np.max(value_mat, axis=0))
    row = np.argmax(np.max(value_mat, axis=1))
    value = value_mat[row][col]
    taken = np.zeros(points.shape[0],dtype=bool)
    for i in range (col,-1,-1):
        if value_mat[row][i]!=value_mat[row][i-1]:
            row=row-points[i-1][3]
            taken[i-1]=1
    taken[0]=1
    return points[taken][:]
