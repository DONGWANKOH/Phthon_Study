import sys
from collections import deque
read=sys.stdin.readline
global N,M,a,visited,res

dr=[-1,-1,0,1,1,1,0]
dc=[0,1,1,1,0,-1,-1]
Q=deque()
Q.append((0,0))


def bfs(r,c):
    visited[r][c] = 1
    Q.popleft((r,c))
    # r=Q[0][0]
    # c=Q[0][1]
    # Q.popleft()
    while len(Q)>0:
        if r==N-1 and c==N-1:
            return
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if a[nr][nc] == 0 or visited[nr][nc] != 0 or a[nr][nc] <= a[r][c]:
                continue
            elif a[nr][nc] > a[r][c]:
                res += 1
            visited[nr][nc] = visited[r][c] + 1


def main():
    global N,M,a,visited,res

    N,M=map(int,read().rstrip().split())
    a=[]
    res=0
    visited=[[0 for c in range(M)] for r in range(N)]
    for i in range(N):
        a.append(list(map(int, read().split())))

    for i in range(N):
        for j in range(M):
            if a[i][j]>=1 and visited[i][j]==0:
                bfs(i,j)
    print(res)

if __name__=='__main__':
    main()