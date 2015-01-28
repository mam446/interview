import random



def maxHeapify(data,cur,length):
    left = 2*cur+1
    right = 2*cur+2
    largest = cur
    if left<length and data[cur]<=data[left]:
        largest = left
    if right <length and data[largest]<=data[right]:
        largest = right
    if largest!=cur:
        data[largest],data[cur] = data[cur],data[largest]
        maxHeapify(data,largest,length)


def makeMaxHeap(data):
    length = len(data)
    for i in xrange(length/2,-1,-1):
        maxHeapify(data,i,length)


def heapSort(data):
    makeMaxHeap(data)
    length = len(data)
    for i in xrange(length,0,-1):
        data[i-1],data[0] = data[0],data[i-1]
        length-=1
        maxHeapify(data,0,length)

def main():
    data = [random.randint(0,100) for i in xrange(10)]

    print data
    heapSort(data)
    print data

if __name__=="__main__":
    main()
