import sys
read=sys.stdin.readline

def getPower(m,n):

    if n==0:
        return 1
    elif n%2==0:
        res=getPower(m,n//2)
        return (res**2)
    else:
        res=getPower(m,n//2)
        return m*(res**2)

def main():
    myList=[int(v) for v in input().split()]
    print(getPower(myList[0],myList[1]))
if __name__== '__main__':
    main()