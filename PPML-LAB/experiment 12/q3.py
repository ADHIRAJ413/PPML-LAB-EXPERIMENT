import matplotlib.pyplot as plt
data=[22,87,5,43,56,73,55,54,11,20,51,5]
plt.hist(data,bins=5,color='purple',label='Histogram Data')
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
data=[7,8,5,6,9,10,15,20,21]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0) # Explode 2nd slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
shadow=True, startangle=140)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z, levels=10, cmap='viridis')
plt.title("Contour Plot")
plt.colorbar()
plt.show()

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 3, 3, 3, 2]
ax.scatter(x, y, z, color='r', label="3D Points")
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.legend()
plt.show()
