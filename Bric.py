import numpy as np
from tqdm import trange
import time
print('initialing...')
a =input('insert your x-w-csv address:').strip('""')
b =input('insert your y-w-csv address:').strip('""')
c =input('insert your z-w-csv address:').strip('""')
print('reading')
for i in trange(100):
    time.sleep(0.005)
print('calculating')
for i in trange(100):
    time.sleep(0.005)
xw = np.loadtxt(open(a,"rb"),delimiter=",",skiprows=2,usecols=[1])
yw = np.loadtxt(open(b,"rb"),delimiter=",",skiprows=2,usecols=[1])
zw = np.loadtxt(open(c,"rb"),delimiter=",",skiprows=2,usecols=[1])
a1 = (xw / 66.25)**2
a2 = (yw / 56.45)**2
a3 = (zw / 42.87)**2
sum = a1+a2+a3
bric = np.sqrt(sum)
print('--------------------------------------------')
print('Max value of Bric :',max(bric))
print('--------------------------------------------')
for i in range(100):
    anwser = input('Do you wanna continue ? y/n:')
    if anwser == 'y':
        a = input('insert your x-w-csv address:').strip('""')
        b = input('insert your y-w-csv address:').strip('""')
        c = input('insert your z-w-csv address:').strip('""')
        print('reading')
        for i in trange(100):
            time.sleep(0.005)
        print('calculating')
        for i in trange(100):
            time.sleep(0.005)
        xw = np.loadtxt(open(a, "rb"), delimiter=",", skiprows=2, usecols=[1])
        yw = np.loadtxt(open(b, "rb"), delimiter=",", skiprows=2, usecols=[1])
        zw = np.loadtxt(open(c, "rb"), delimiter=",", skiprows=2, usecols=[1])
        a1 = (xw / 66.25) ** 2
        a2 = (yw / 56.45) ** 2
        a3 = (zw / 42.87) ** 2
        sum = a1 + a2 + a3
        bric = np.sqrt(sum)
        print('--------------------------------------------')
        print('Max value of Bric :', max(bric))
        print('--------------------------------------------')
    else:
        print("You have chosen to quit this program")
        quit()





