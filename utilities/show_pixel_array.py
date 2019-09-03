# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:32:29 2019

@author: msobot
"""

from PIL import Image
import numpy as np


filename = "train.txt"
Dir = "C:\py_src\data\digit"
w, h = 16, 16
data = np.zeros((h, w), dtype=np.uint8)

fname = Dir+"\\"+filename
fp = open(fname,"r")
k = 0
# 2 is the number of lines you want to read
while k < 2:
    
    line = fp.readline()
    #print line
    num = line.split(",")
    print len(num)
    i = 0
    j = 0
    cnt = 0
    while i < 16:
        j = 0
        while j < 16:
            # need to bound between 0 - 255
            data[i,j] = (float(num[cnt])+1.0) *127.5
            cnt+=1
            j+=1
        i+=1
    img = Image.fromarray(data, 'L')
    name = Dir+"//"+"zero"+"_"+str(k)+".png"
    img.save(name)
    k+=1
    # if you save the png, showing is optional
    img.show()
    

