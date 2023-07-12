# -*- coding: utf-8 -*-
"""
Buck converter with current-mode control
"""
from math import pi, log10
from control import tf, bode_plot, margin, step_response
import matplotlib.pyplot as plt
# Create Laplace variable
s = tf('s')

Vi=12
L= 100e-6; C=10e-6; rc=200e-3
R=5

Gc= R*(1 + rc*C*s)/(1 + (R+rc)*C*s)

fz= 1/(2*pi*rc*C); fp= 1/(2*pi*(R+rc)*C)

print("fz= ", fz)
print("fp= ", fp)

# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz

mag, phase, omega = bode_plot(Gc, dB=True, Hz=True, omega_limits=(10,100e3), \
                              omega_num=100 )
i=25
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=50
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=75
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=82
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)





















