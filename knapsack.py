import numpy as np

#knapsack Problem using dynamic algorithm, Takes weights, values of items and capacity as input and returns item chosen 

def knpsck_value_mat(data,capacity):  # creates value_matrix for full capacity
    value_mat=np.zeros((capacity+1,data.shape[0]+1), dtype=np.int)
    for item in range (data.shape[0]):
        for weight in range(1,int(data[item][3])):
            value_mat[weight][item+1]= value_mat[weight][item]
        for weight in range(int(data[item][3]),capacity+1):
            value_mat[weight][item+1]= max(data[item][2]+value_mat[weight-data[item][3]][item],value_mat[weight][item])
    return value_mat
            

def knpsck_select_items(value_mat,capacity,data): #Gives points to be selected for given capacity and value_matrix
    value_mat=value_mat[:capacity+1,:]
    col = np.argmax(np.max(value_mat, axis=0))
    row = np.argmax(np.max(value_mat, axis=1))
    value = value_mat[row][col]
    selected = np.zeros(value_mat.shape[0],dtype=bool)
    for i in range (col,-1,-1):
        if value_mat[row][i]!=value_mat[row][i-1]:
            row=row-data[i-1][3]
            selected[i-1]=1
    selected[0]=1
    return selected
