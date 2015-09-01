import numpy as np
import xlrd

def read(path):
    book = xlrd.open_workbook(path)
    worksheet = book.sheet_by_index(0)
    points=np.zeros((worksheet.nrows,worksheet.ncols))
    for i in range (worksheet.nrows):
        for j in range (worksheet.ncols):
            points[i][j]=worksheet.cell(i,j).value
    return points

def find_distance(points):
    distance=np.zeros((points.shape[0],points.shape[0]))
    for i in range(points.shape[0]):
        for j in range (i+1, points.shape[0]):
            distance[i][j]=pow(pow(points[i][0]-points[j][0],2)+pow(points[i][1]-points[j][1],2),0.5)
            distance[j][i]=distance[i][j]
    return distance

def find_segment_length(route,distance):
    segments=np.zeros(route.shape[0]-1)
    for i in range(route.shape[0]-1):
        segments[i]=distance[route[i]][route[i+1]]
    return segments
