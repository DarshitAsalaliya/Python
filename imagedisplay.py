# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:02:35 2020

@author: vajok
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

print(os.chdir("D:\datasetDS"))
img = plt.imread('elephant.JPG')
img.shape, img.dtype
plt.imshow(img)
plt.savefig('plot.JPEG')
