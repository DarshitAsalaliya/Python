# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:53:00 2020

@author: vajok
"""
import numpy as np
import matplotlib.pyplot as pltured_time = np.linspace(0, 1, 10)

meas

noise = (np.random.random(10)*2 - 1) * 1e-1

measures = np.sin(2 * np.pi * measured_time) + noise 

from scipy.interpolate import interp1d
linear_interp = interp1d(measured_time, measures)
plt.plot(measured_time)

#plt.plot(measures)

interpolation_time = np.linspace(0, 1, 50)
linear_results = linear_interp(interpolation_time)
plt.plot(interpolation_time)
plt.plot(linear_results)
