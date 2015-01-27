


def one(string):
    return string[::-1]

def two(string):
    return ' '.join(string.split(' ')[::-1])

def three(string):
    return ' '.join(map(lambda x: x[::-1],string.split(' ')))





if __name__=="__main__":
    x = "Hi my name is Bob"


    print one(x)
    print two(x)
    print three(x)

