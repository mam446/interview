



class singleNode(object):
    def __init__(self,data,child=None):
        self.forward = child
        self.data = data

class singleList(object):
    def __init__(self):
        self.head=None
        self.length = 0


    def push(self,data):
        self.head = singleNode(data,self.head)
        self.length+=1

    def pop(self):
        cur = self.head
        if cur:
            self.head = self.head.forward
            self.length-=1
            return cur.data
        return None

    def remove(self,data):
        cur = self.head
        if cur.data ==data:
            self.head = self.head.forward
            self.length-=1
            return True

        while cur.forward and cur.forward.forward and cur.forward!=data:
            cur = cur.forward
        if cur.forward and cur.forward.data==data:
            cur.forward = cur.forward.forward
            self.length-=1
            return True
        else:
            return False



    def clear(self):
        self.head = None
        self.length = 0

    def toList(self):
        ret = []
        cur = self.head
        while cur:
            ret.append(cur.data)
            cur = cur.forward
        return ret


    def reverse(self):
        new = None
        cur = self.head
        nxt = None
        while cur.forward:
            nxt = cur.forward
            cur.forward = new
            new = cur
            cur = nxt
        cur.forward = new
        self.head = cur









