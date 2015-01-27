import random





def changePoss(amount,denominations):
    ways = [0]*(amount+1)
    ways[0] = 1

    for coin in denominations:
        for high in xrange(coin,amount+1):
            remainder = high-coin
            ways[high]+=ways[remainder]
    return ways[amount]





def test():
    print changePoss(5,[1,3,5])
    return









if __name__=="__main__":
    test()
