import matplotlib.pyplot as plt

def plotTSP(path, points,data):
    
    # Unpack the primary TSP path and transform it into a list of ordered 
    # coordinates

    x = []; y = []
    x_all=[];y_all=[]
    for i in path:
        x.append(points[i][0])
        y.append(points[i][1])
    for i in range (data.shape[0]):
        x_all.append(data[i][0])
        y_all.append(data[i][1])
    plt.plot(x_all, y_all, 'co')

    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x))/float(100)

        # Draw the primary path for the TSP problem
    plt.arrow(x[-2], y[-2], (x[0] - x[-2]), (y[0] - y[-2]), head_width = 10*a_scale, 
            color ='g', length_includes_head=True)
    for i in range(0,len(x)-2):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = 10*a_scale,
                color = 'r', length_includes_head = True)

    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(min(x_all)*1.1, max(x_all)*1.1)
    plt.ylim(min(y_all)*1.1, max(y_all)*1.1)
    plt.show()
