import sys





def power(x,y):
    if not y:
        return 1
    if y==1:
        return x
    t = power(x,y/2)
    if y%2:
        return t*t*x
    else:
        return t*t


if __name__=="__main__":
    print power(int(sys.argv[1]),int(sys.argv[2]))








