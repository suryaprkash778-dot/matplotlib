import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
fig = plt.figure(figsize=(3,2))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='r',ls='-',marker='*')
ax.set_xlabel('X axis')
ax.set_ylabel('y axis')
ax.set_title('Graph')


plt.show()
