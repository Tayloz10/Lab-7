#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
def rule4(Q, Ae, Be, Aun, Bun, A, B):
    Qun = np.abs(Q) * np.sqrt(((Ae * Aun / A) ** 2) + ((Be * Bun / B) ** 2))
    return Qun
def stdun(x):
    stdun = np.std(x) / np.sqrt(x.size)
    return stdun
# Variables, V=volts, T=seconds, c=charge, d=discharge
# Part 1, 13 values per array.
Vcplot = np.array([0.00, 3.57, 6.17, 7.83, 8.99, 9.73, 10.23, 10.57, 10.84, 10.99, 11.10, 11.19, 11.25])
Tcplot = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
Vdplot = np.array([11.42, 7.86, 5.28, 3.61, 2.44, 1.68, 1.14, 0.79, 0.54, 0.38, 0.26, 0.18,0.13])
Tdplot = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
# Part 2, 10 values per array.
Vo = 11.45
Tc = np.array([29.43, 29.96, 29.65, 29.43, 29.71, 29.06, 29.15, 29.62, 29.37,29.65])
Td = np.array([26.12, 26.87, 26.75, 27.25, 26.75, 27.21, 26.90, 27.00, 26.81,26.78])
# Part 3
Ohms = 500.6e3
Ohm_un = .05e3
Farads = 53.8e-6
Farad_un = .05e-6
# Part 1
plt.plot(Tcplot, Vcplot);
plt.ylabel('Voltage (volts)');
plt.xlabel('Time (seconds)');
plt.title('Charging Capacitor')
plt.show()
plt.plot(Tdplot, Vdplot);
plt.ylabel('Voltage (volts)');
plt.xlabel('Time (seconds)');
plt.title('Discharging Capacitor')
plt.show()
# Part 2
Vc_theoretical = .632 * Vo
Vd_theoretical = .368 * Vo
Tc_avg = np.mean(Tc);
Tc_avgun = stdun(Tc)
Td_avg = np.mean(Td);
Td_avgun = stdun(Td)
# print('Our theoretical values for voltage after one time constant when charging and discharging were, respectively,', '%.2f' % Vc_theoretical,'and\
# ', '%.2f' % Vd_theoretical,'.')
print('Our average charge time to', '%.2f' % Vc_theoretical, ' volts was', '%.2f' % Tc_avg, '+/-', '%.2f' % Tc_avgun, 'seconds.\nOur average discharge time to', '%.2f' % Vd_theoretical, 'volts was', '%.2f' % Td_avg, '+/-', '%.2f' % Td_avgun,
      'seconds.')
# Part 3
Tconstant = (Ohms * Farads);
Tconstant_un = rule4(Tconstant, 1, 1, Ohm_un, Farad_un, Ohms, Farads)
print('\nOur theoretical time constant was', '%.2f' % Tconstant, '+/-', '%.2f' % Tconstant_un, 'seconds.')


# In[ ]:




