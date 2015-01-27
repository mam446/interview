import random
import time
import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt

def checkTruth(data):
    best = (0,0)
    s = None
    for i in xrange(len(data)):
        tempSum = 0
        for j in xrange(i,len(data)):
            tempSum += data[j]
            if not s or tempSum>s: 
                s = tempSum
                best = (i,j+1)
    return best

def mySol(data):
    running = [0]
    d = 0
    q = len(data)
    for i in xrange(q):
        d+=data[i]
        running.append(d)
    s = None
    m = 0
    best = None
    for i in xrange(q):
        temp = running[i+1]-running[m]
        if not s or temp>s:
            best = (m,i+1)
            s = temp
        if  running[i+1]<running[m]:
            m = i+1
    return best

x = []
time1 = []
time2 = []
runs = 10
if len(sys.argv) >2:
    runs = int(sys.argv[2])
size =  int(sys.argv[1])
for i in xrange(10,int(size)):
    d1 = 0
    d2 = 0
    for k in xrange(runs):
        y = [random.randint(-1000,1000) for j in xrange(i)]

        

        s1 = time.time()
        truth = checkTruth(y)
        e1 = time.time()
        s2 = time.time()
        my = mySol(y)
        e2 = time.time()
        d1+=e1-s1
        d2+=e2-s2
        if truth!=my:
            print truth
            print my
            raw_input()
    time1.append(d1/float(runs))
    time2.append(d2/float(runs))
    x.append(i)


plt.figure(1)
ax = plt.subplot(111)
ax.plot(x,time1,x,time2)

plt.savefig("sumSeq.png")
plt.show()


