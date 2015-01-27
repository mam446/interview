






def merge(data):
    data = sorted(data,key=lambda x: x[0])
    cur = 0
    while True:
        if cur>=len(data)-1:
            break
        if data[cur+1][0]<=data[cur][1]:
            data[cur+1] = (data[cur][0],max([data[cur][1],data[cur+1][1]]))
            data.remove(data[cur])
        else:
            cur+=1
    return data

if __name__=="__main__":
    data = [(0,1),(3,5),(4,8),(10,12),(9,10)]
    print merge(data)

    data = [(1,2),(2,3)]
    print merge(data)

    data = [(1,10),(2,6),(3,5),(7,9)]
    print merge(data)

    data = [(1,3),(2,4)]
    print merge(data)
    data = [(1,5),(2,3)]
    print merge(data)

