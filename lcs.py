



def lcs(string1, string2,grid=None):
    n = len(string1)
    m = len(string2)
    grid =[[0]*(m+1) for i in xrange(n+1)]
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            if string1[j-1]==string2[i-1]:
                grid[j][i] = grid[j-1][i-1]+1 
            elif grid[j][i-1]>=grid[j-1][i]:
                grid[j][i] = grid[j][i-1]
            else:
                grid[j][i] = grid[j-1][i]
    printGrid(grid)
    return grid,grid[-1][-1]


def printGrid(grid):
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            print grid[i][j],
        print


def existsIn( search,string):
    grid,length = lcs(search,string)
    print len(search),length
    ret = length==len(search)
    return ret



def test():
    print existsIn('adfjk','asdfghjkl')
    print existsIn('adfjkl','asdfghjkl')
    
    
    
    return



if __name__=="__main__":
    test()













