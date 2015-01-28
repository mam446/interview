import random

def rotate(matrix):
    x = len(matrix)
    y = len(matrix[0])
    data = [[0]*x for i in xrange(y)]
        
    for i in xrange(x):
        for j in xrange((y)):
            data[j][i] = matrix[i][j]
    return data


def rotateClockwise(matrix):
    n = len(matrix)
    for j in xrange(n/2): 
        for i in xrange(j,n-1-j):
            a = matrix[j][i]
            b = matrix[i][n-1-j]
            c = matrix[n-1-j][n-1-i]
            d = matrix[n-1-i][j]
        
        
            matrix[j][i] = d
            matrix[i][n-1-j] = a
            matrix[n-1-j][n-1-i] = b
            matrix[n-1-i][j] = c


def printMatrix(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            print matrix[i][j],
        print

def main():
    x = [[random.randint(0,10) for i in xrange(5)] for j in xrange(3)]
    #y = rotate(x)
    printMatrix(x)
    print 
    print

    printMatrix(zip(*x[::-1]) )
    #printMatrix(zip(*x)[::-1] )
    #rotateClockwise(x)
    print
    printMatrix(x)

if __name__=="__main__":
    main()
