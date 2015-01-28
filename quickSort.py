import random

def quickSort(data,start,end):
    if start<end:
        p = partition(data,start,end)
        quickSort(data,start,p-1)
        quickSort(data,p+1,end)

def partition(data,start,end):
    x = data[end]
    p = start

    for j in xrange(start,end):
        if data[j]<=x:
            data[p],data[j] = data[j],data[p]
            p+=1
    data[p],data[end] = data[end],data[p]
    return p



def main():
    data = [random.randint(0,100) for i in xrange(30)]


    print data
    quickSort(data,0,len(data)-1)
    print data





if __name__=="__main__":
    main()
