import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**9)

def cal(a,b,c):
    if b==1:
        return a%c
    else :
        ans=cal(a,b//2,c)
        if b%2==0:
            return ans*ans%c
        else :
            return ans * ans *a % c
# res=cal(a,b,c)

def main():
    global cnt
    cnt = 0
    A, B, C = map(int, read().split())
    print(cal(A, B, C))

if __name__=='__main__':
    main()