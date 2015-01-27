import unittest
import random
import linkedList

class ListTestCase(unittest.TestCase):
    def setUp(self):
        self.l = linkedList.singleList()
    


    def test_push(self):
        cur = None
        last = random.randint(0,100)
        self.l.push(last)
        self.assertEqual(self.l.head.data,last,'Initial Push does not work')
        for i in xrange(1000):
            cur = random.randint(0,100)
            self.l.push(cur)
            self.assertEqual(self.l.head.data,cur,'Subsequent push does not push correct data')
            self.assertEqual(self.l.head.forward.data,last,'Subsequent push does not connect list correctly')
            last = cur

    def test_pop(self):
        data = range(1000)

        for d in data:
            self.l.push(d)

        for d in data[::-1]:
            cur = self.l.pop()
            self.assertEqual(cur,d,'pop is not popping off the right object')


       
    def test_check_length(self):
        for i in xrange(1000):
            self.l.push(random.randint(0,100))
            self.assertEqual(self.l.length,i+1,'length does not update correctly on push')

        



    def test_clear(self):
        for i in xrange(1000):
            self.l.push(random.randint(0,100))
        self.l.clear()
        self.assertEqual(self.l.head,None,'Head node not set to None on clear')
        self.assertEqual(self.l.length,0,'Length does not reset on clear')

def suite():
    tests = ['test_push','test_pop','test_check_length','test_clear']

    return unittest.TestSuite(map(ListTestCase,tests))



if __name__=="__main__":
    if suite():
        print "Passed All Tests"











