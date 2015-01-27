import random
import sys
import time
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt



def findPalindrome2(string):
    if not string:
        return None
    if len(string)==1:
        return string


    length = len(string)
    maxLen = 0
    longestStr = None
    table = [[1]*length for i in xrange(length)]


    for i in xrange(length-2):
        if string[i]==string[i+1]:
            table[i][i+1] = 1
            longestStr = string[i:i+2]

    for l in xrange(3,length):
        for i in xrange(0,length-l):
            j = i+l-1
            if string[i]==string[j]:
                table[i][j] = table[i+1][j-1]
                if table[i][j]==1 and l>maxLen:
                    longestStr = string[i:j+1]
            else:
                table[i][j] = 0
    return longestStr


def findPalindrome(string):
    best = None
    for i in xrange(len(string)-1):
        #one center
        one = helperFunction(string,i,i)
        if not best or one[1]-one[0]>best[1]-best[0]:
            best = one
        #two center
        two = helperFunction(string,i,i+1)

        if not best or two[1]-two[0]>best[1]-best[0]:
            best = two
    return best


def helperFunction(string,begin, end):
    while begin>=0 and end<len(string) and string[begin]==string[end]:
        begin-=1
        end+=1
    return (begin+1,end)





def test():
   
    runs = 100
    size = int(sys.argv[1])
    time1 = []
    time2 = []
    x = []
    z = []
    for i in xrange(10,int(size)):
        d1 = 0
        d2 = 0
        for k in xrange(runs):
            y = "".join([random.choice(['a']) for j in xrange(i)])
            s1 = time.time()
            r1 = findPalindrome(y)
            e1 = time.time()
            d1+=e1-s1
            d2+=r1[1]-r1[0]
        time1.append(d1/runs)
        z.append(d2/float(runs))
        x.append(i)
        s1 = time.time()
        #for k in xrange(runs):
        #    r1 = findPalindrome2(y)
            
        e1 = time.time()
        time2.append(e1-s1)
        print x[-1],time1[-1]

    plt.figure(1)
    ax = plt.subplot(211)
    ax.plot(x,time1,x,time2)
    ax = plt.subplot(212)
    ax.plot(x,z)

    plt.savefig("pal.png")
    plt.show()

    
    
    
    return







if __name__ =="__main__":
    test()




