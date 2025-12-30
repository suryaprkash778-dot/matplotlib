import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.4,0.4])
axes1.plot(x,y)
axes1.set_xlabel('X axis')
axes1.set_ylabel('y axis')
axes1.set_title('Graph')

axes2 = fig.add_axes([0.5,0.1,0.4,0.4])
axes2.plot(y,x)
axes2.set_xlabel('X axis')
axes2.set_ylabel('y axis')
axes2.set_title('Graph')

plt.show()
