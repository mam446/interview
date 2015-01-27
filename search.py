


def bfs(grid):
    start = (0,0)
    end = (len(grid)-1,len(grid)-1)
    visited = set()
    toVisit = [start]
    double = []
    visited.add(start)
    while toVisit:
        cur = toVisit.pop(0)
        double.append(cur)
        #print cur
        #print toVisit
        #raw_input()
        if cur==end:
            print len(double)
            return True
        if cur[0]!=0:
            if (cur[0]-1,cur[1]) not in visited:
                toVisit.append((cur[0]-1,cur[1]))
                visited.add((cur[0]-1,cur[1]))
        if cur[1]!=0:
            if (cur[0],cur[1]-1) not in visited:
                toVisit.append((cur[0],cur[1]-1))
                visited.add((cur[0],cur[1]-1))

        if cur[0]!=len(grid)-1:
            if (cur[0]+1,cur[1]) not in visited:
                toVisit.append((cur[0]+1,cur[1]))
                visited.add((cur[0]+1,cur[1]))
        if cur[1]!=len(grid)-1:
            if (cur[0],cur[1]+1) not in visited:
                toVisit.append((cur[0],cur[1]+1))
                visited.add((cur[0],cur[1]+1))
    print len(double)
    return False 

def dfs(grid):
    start = (0,0)
    end = (len(grid)-1,len(grid)-1)
    visited = set()
    toVisit = [start]
    double = []
    visited.add(start)
    while toVisit:
        cur = toVisit.pop(len(toVisit)-1)
        double.append(cur)
        #print cur
        #print toVisit
        #raw_input()
        if cur==end:
            print len(double)
            return True
        if cur[0]!=0:
            if (cur[0]-1,cur[1]) not in visited:
                toVisit.append((cur[0]-1,cur[1]))
                visited.add((cur[0]-1,cur[1]))
        if cur[1]!=0:
            if (cur[0],cur[1]-1) not in visited:
                toVisit.append((cur[0],cur[1]-1))
                visited.add((cur[0],cur[1]-1))

        if cur[0]!=len(grid)-1:
            if (cur[0]+1,cur[1]) not in visited:
                toVisit.append((cur[0]+1,cur[1]))
                visited.add((cur[0]+1,cur[1]))
        if cur[1]!=len(grid)-1:
            if (cur[0],cur[1]+1) not in visited:
                toVisit.append((cur[0],cur[1]+1))
                visited.add((cur[0],cur[1]+1))
    print len(double)
    return False 

def test():
    n = 10
    grid = [[0]*n for i in xrange(n)]
    bfs(grid)
    dfs(grid)
    return
    

if __name__=="__main__":
    test()





















