import copy
import random
import sys


class node(object):
    def __init__(self,data,nextNode=None):
        self.forward = nextNode
        self.data = data

def reverse(sll):
    newList = None
    curNode = sll
    while curNode:
        nextNode = curNode.forward
        curNode.forward = newList
        newList = curNode
        curNode = nextNode
    return newList 


def printList(data):
    cur = data
    while cur!=None:
        print cur.data,
        cur = cur.forward
    print

def makeList(data):
    cur =None
    for i in xrange(len(data)):
        cur = node(data[-i-1],cur)
    return cur


def main():
    length = int(sys.argv[1])
    x = [random.randint(0,10) for i in xrange(length)]
    linked_list = makeList(x)
    printList(linked_list)
    printList(reverse(reverse(linked_list)))

if __name__ =="__main__":
    main()

