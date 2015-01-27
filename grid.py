import random

def printGrid(grid):
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            print grid[i][j],
        print

def summer(gridSum,i,j):
    l = []
    #down
    print i
    if i!=len(gridSum)-1:
        l.append(gridSum[i+1][j])
    #diag
    if i!=len(gridSum)-1 and j!=len(gridSum[i])-1:
        l.append(gridSum[i+1][j+1])

    #right
    if j!=len(gridSum[i])-1:
        l.append(gridSum[i][j+1])
    if not l:
        return 0
    return max(l)

def summer2(gridSum,i,j):
    l = []
    #down
    print i
    if i!=0:
        l.append(gridSum[i-1][j])
    #diag
    if i!=0 and j!=0:
        l.append(gridSum[i-1][j-1])

    #right
    if j!=0:
        l.append(gridSum[i][j-1])
    if not l:
        return 0
    return max(l)


def calcGrid(grid,gridSum):
    n = len(grid)
    m = None
    if n:
        m = len(grid[0])

    for i in xrange(n):
        j = m-1
        k = n-1-i
        while k<n:
            gridSum[k][j] = grid[k][j]+summer(gridSum,k,j)
            j-=1
            k+=1

    for i in xrange(1,m):
        j = m-1-i
        k = 0
        while k<n and j>=0:
            gridSum[k][j] = grid[k][j]+summer(gridSum,k,j)
            j-=1
            k+=1
    return grid, gridSum

def calcGrid2(grid,gridSum):
    n = len(grid)
    m = None
    if n:
        m = len(grid[0])

    for i in xrange(n):
        for j in xrange(m):
            j = m-j-1
            k = n-i-1
            gridSum[k][j] = grid[i][j]+summer(gridSum,k,j)
    return grid, gridSum


def main():
    m = 10
    n = 10

    grid = [[random.randint(-100,100) for i in xrange(m)]for j in xrange(n)]
#grid = [[random.randint(0,10) for i in xrange(m)]for j in xrange(n)]
    gridSum = [[0]*m for i in xrange(n)]
    
    grid2,gridSum2 = calcGrid(grid,gridSum)
    grid3,gridSum3 = calcGrid2(grid,gridSum)
    print
    printGrid(gridSum3)
    printGrid(gridSum2)


if __name__=="__main__":
    main()












