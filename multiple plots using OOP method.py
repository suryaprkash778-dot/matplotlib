import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y,'r',ls='-',marker='+')
axes[0].set_title('first plot')

axes[1].plot(y,x,'b',ls='--',marker='*')
axes[1].set_title('second plot')
plt.tight_layout()
plt.show()
