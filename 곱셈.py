# 10 11 12
import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**9)
# 10 11 12 제곱된 수, 반복 수

def cal(a,b,c,res,cnt):
    res=res*a
    cnt += 1
    print('전',a, b, c, res, cnt)

    if res>=c or cnt==b:
        ans=res%c
        return ans

    cal(a, b, c, res, cnt)

    print('후',a,b,c,res,cnt)

def main():
    global cnt
    cnt=0
    A, B, C = map(int, read().split())
    print(cal(A,B,C,1,cnt))

if __name__=='__main__':
    main()

