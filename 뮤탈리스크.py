import sys
from collections import*
read=sys.stdin.readline
global N,data,scv,res

attack=[9,3,1]
scv=[]
scv_after=[]
res=0


def bfs(data):
    global N, scv, res
    Q = deque()
    data = sorted(data, key=lambda x: x[0], reverse=True)
    Q.append(data[0])
    visited[0]=0
    attack_num=0

    while len(Q)>0:
        data = sorted(data, key=lambda x: -x[0], reverse=True)
        svc=Q.popleft(data[0])
        for i in range(3):
            if svc<j or visited[a]!=0:
                continue
            data-=attack[i]
            attack_num+=1

            visited[a+1]=visited[a]+1
            Q.append(data[n+1])

            scv.append(j)

  #scv에 저장되는 값들


def main():
    global N,data,scv,res
    N=int(input())
    data=list(map(int,read().rstrip().split()))

    bfs(data)

    print(scv)

if __name__=='__main__':
    main()