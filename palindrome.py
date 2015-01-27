import sys




def checkPalindrome(word):
    return word==word[::-1]











if __name__=="__main__":
    print checkPalindrome(sys.argv[1])


