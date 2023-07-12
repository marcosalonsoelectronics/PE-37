# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:57:33 2023

@author: Alonso
"""
from math import sqrt, ceil, pi
import matplotlib.pyplot as plt
import numpy as np

Vi=12
L= 100e-6; C=10e-6
R=5

def Vof(Ipeak, f): 
    return (1+2*L*f/R)*Vi/2 - 0.5*sqrt( (1+2*L*f/R)**2*Vi**2 - 8*L*f*Vi*Ipeak  )  


# Define plotting range and step
xmin=0.1; xmax=2; step=0.1
npoints = ceil( (xmax-xmin)/step ) # rounds up to nearest integer

# Create arrays
Ipeak =   np.arange(xmin, xmax, step, dtype=np.float)
Vo    =   np.arange(xmin, xmax, step, dtype=np.float)

# Calculate values
for i in range (0, npoints):
    Vo[i]  = Vof(Ipeak[i], 100e3)
    print(Ipeak[i], Vo[i])
    
print("Vo= ", Vof(1.8, 100e3))
print("D= ", Vof(1.8, 100e3)/Vi)
    
# Plot the function
plt.figure(1)
plt.plot(Ipeak, Vo, 'red')
plt.grid(True)
plt.xlabel("Ipeak, A")
plt.ylabel("Vo, V")
#plt.title(r"My Function, $\alpha$")
# plt.ylim(-1.5,1.5)
# plt.xlim(0,3*pi)
# plt.text(3, 0.8, "My sine function", size=10, color="red", backgroundcolor='yellow')
# plt.savefig("Sine.png", dpi=300)


