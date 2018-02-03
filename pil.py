# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 09:36:35 2017

@author: snall
"""
from PIL import Image
import os,glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file = glob.glob('H:/照片/DCIM/.thumbnails/*.jpg')[0]
im = Image.open(file)
color=im.histogram()
#print (b)

r,g,b = color[:256],color[256:512],color[512:]

rnp = np.array(r)


rs,gs,bs = pd.Series(r),pd.Series(g),pd.Series(b)
plt.plot(rs.index,rs)
plt.bar(rs.index,rs)
plt.title('red')
plt.show()










im.convert('L')
im.save('H:/照片/DCIM/.thumbnails/'+'8bitstest'+'.jpg')
