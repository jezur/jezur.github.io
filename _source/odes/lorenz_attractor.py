"""
Lorenz system of ODEs. 
Created on Sun Jul 11 21:39:25 2021
@author: j
"""
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


# Lorenz system of equations. Strange atractor. Parameters sigma, beta and rho
# are specified directly. 
def lorenz(state, t, sigma=10.0, beta=8.0/3.0, rho=28.0):
    x, y, z = state     
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


# We are gonna solve the lorenz system for 9 initial conditions. We want the 
# butterfly shape fast, and that is why we use many initial conditions. All 
# will be random numbers between -15 and 15. We use a seed for the 
# np.random.random function so the graphics are the same allways. The 
# simulation time will be of 20 units of time, using 8000 points.
np.random.seed(10) # Try: 6, 7, 10*, 15
N   = 9
x0  = -15 + 30 * np.random.random((N, 3))
t   = np.linspace(0, 20, 8000)


# Solutions to Lorenz are stored in a tensor. Results will all be ploted in a
# 3D projection using matplotlib
xt  = np.asarray([odeint(lorenz, i, t) for i in x0])


# Figure object of one axis only. All will be 3D projections on a plane. We 
# turn off the axis so we only wet the plot. We define the limits of the plot.
fig = plt.figure(figsize=(12, 12))
ax  = fig.add_subplot(1, 1, 1, projection='3d')
ax.axis('off')
ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))


# Each solution curve in phase space will be plotted with a color. All collors
# used are in this list:
colors = ['darkslategray', 'slateblue', 'blue', 'navy', 'black', 'gray',
          'silver','royalblue','gainsboro']


# Using a forloop we plot all sets of points in the solution tensor. We pick 
# the colors for each curve in order
for i in range(N):
    ax.plot3D(xt[i,:,0], xt[i,:,1], xt[i,:,2], colors[i])

# We set the angles at which we see the 3D plot. Then we save a transparent 
# image to be used in the CV
ax.view_init(-25, -40)
name = "lorenz_attractor.png"
plt.savefig(name, transparent=True, dpi=300, bbox_inches=0.0, pad_inches=0.0)
plt.show()
print('The PNG image may be cropped later.')
