import time
import sys
import matplotlib
#matplotlib.use('Agg')
import math
import matplotlib.pyplot as plt



def findDrop(length,numEggs,first =False):
    if numEggs == 1:
        return ([1],length)
    if length <=2:
        return ([1],length)
    best =None
    bt = None
    l = []
    for ps in xrange(2,length):
        nextSize = ps-1
        myDrops = length/ps
        future = findDrop(nextSize,numEggs-1)
        total = myDrops+future[1]
        l.append(([ps]+future[0],total,))
        if not bt or total<=bt:
            bt = total
            best = ([ps]+future[0],total)
        else:
            continue
            break
    if first:
        return l
    return best









def main():

    eggs = 2
    x = []
    time1 = []
    time2 = []
    time3 = []
    runs = 1000
    m = int(sys.argv[1])
    if len(sys.argv)>2:
        runs = int(sys.argv[2])
    for i in xrange(10,int(m)):
        a = findDrop(i,2)
        time3.append(math.log(i,2))
        time2.append(math.floor(2*i**(1.0/2))-1)
        time1.append(a[1])
        x.append(i)
        """
        start = time.time()
        for k in xrange(runs):
            a = findDrop(i,eggs+1)
        
        end = time.time()
        time2.append((end-start)/runs)

        start = time.time()
        for k in xrange(runs):
            a = findDrop(i,eggs+2)
        
        end = time.time()
        time3.append((end-start)/runs)
        """
    plt.figure(1)
    ax = plt.subplot(111)
    #ax.plot(x,time1)
    ax.plot(x,time1,x,time2,x,time3)

    plt.savefig("eggs.png")
    plt.show()


def main2():
    x = findDrop(200,int(sys.argv[1]),True)
    print x
    plt.figure(1)
    ax = plt.subplot(111)
    ax.plot(range(len(x)),map(lambda x:x[1],x))
    #ax.plot(x,time1,x,time2,x,time3)

    #plt.savefig("eggs.png")
    plt.show()

if __name__=="__main__":
    main()





