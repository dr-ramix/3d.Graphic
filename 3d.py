import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-4,4,0.4)

y=np.arange(-4,4,0.4)
X,Y=np.meshgrid(x,y)
Z=(1.8**(-1.5*np.sqrt(X**2+Y**2))*np.cos(0.5*Y)*np.sin(X))
figure=plt.figure(figsize=(8,8))
ax=figure.add_subplot(111,projection='3d')
u=ax.plot_surface(X,Y,Z,cmap=plt.cm.gist_earth,
                       linewidth=0, antialiased=True)
figure.colorbar(u)
plt.show()