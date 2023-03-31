#시간 복잡도 O(N^2)
import sys
read=sys.stdin.readline

def solution(n,s):
    res=[]
    answer=[]
    ans=[0 for _ in range(n+1)]
    l=len(s)
    for i in range(1,n+1):
        l=l-s.count(i-1)
        r=s.count(i)
        ans[i]=r/l
    ans=ans[1:]

    for j in enumerate(ans, start=1):
        res.append(j)
    res=sorted(res, key=lambda x: x[1], reverse=True)

    for k in res:
        answer.append(k[0])

    return answer

def main():
    N=int(read())
    stage=list(map(int,read().split()))
    print(solution(N,stage))

if __name__=='__main__':
    main()