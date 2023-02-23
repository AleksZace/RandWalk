import matplotlib.pyplot as plt
import random 
for i in range(1000):
    y=[0,0]
    x = random.randint(1,4)
    if x == 1:
        xPoints = [y[0],y[0]+1]
        yPoints = [y[1],y[1]]
        plt.plot(xPoints,yPoints)
        y = [xPoints[1],yPoints[1]]
    if x == 2:
        xPoints = [y[0],y[0]-1]
        yPoints = [y[1],y[1]]
        plt.plot(xPoints,yPoints)
        y = [xPoints[1],yPoints[1]]
    if x == 3:
        xPoints = [y[0],y[0]]
        yPoints = [y[1],y[1]+1]
        plt.plot(xPoints,yPoints)
        y = [xPoints[1],yPoints[1]]
    if x == 4:
        xPoints = [y[0],y[0]]
        yPoints = [y[1],y[1]-1]
        plt.plot(xPoints,yPoints)
        y = [xPoints[1],yPoints[1]]
plt.show()
