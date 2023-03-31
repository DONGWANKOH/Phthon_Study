
import sys
from collections import deque

read=sys.stdin.readline

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def check():  # arr에 연속으로 1이 들어지 않는 곳만 0으로 만든다..
    global visited, arr, N, M, Q
    cnt=1
    while Q:
        r=Q[0][0]
        c=Q[0][1]
        Q.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]

            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 1 and cnt==1:
                # print('1:들어감')
                arr[nr][nc] = 0
                cnt =0

            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
                # print('2:들어감')
                Q.append((nr,nc))
                visited[nr][nc]=visited[r][c]+1


def bfs():
    global visited,arr,N,M,Q
    cnt=1
    while Q:
        r=Q[0][0]
        c=Q[0][1]
        Q.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]

            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 1 and cnt==1:
                # print('1:들어감')
                arr[nr][nc] = 0
                cnt =0

            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
                # print('2:들어감')
                Q.append((nr,nc))
                visited[nr][nc]=visited[r][c]+1

def main():
    global visited, arr, N, M,Q,point
    Q=deque()
    N,M=map(int,read().split())
    arr=[list(map(int,read().rstrip())) for _ in range(N)]
    visited=[[[[0]*2]*M]* N]
    point = []
    print(visited)
    visited[0][0] = 1
    Q.append((0,0))
#############################################################

    check()

    bfs()
    # print(point)

    # if visited[N-1][M-1]==0:
    #     print(-1)
    # else:
    #     print(visited[N-1][M-1])


if __name__=='__main__':
    main()