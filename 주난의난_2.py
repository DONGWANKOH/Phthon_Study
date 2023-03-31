import sys
from collections import deque
read=sys.stdin.readline


dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c):
    global bar_x,bar_y
    visited[r][c]=1
    if r==bar_x-1 and c==bar_y-1:
        return True
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc]==0 and visited[nr][nc]==0:
            dfs(nr,nc)
            # return True
    return False

def check(bar_x,bar_y):
    global arr
    if arr[bar_x-1][bar_y-1]=='#':
        for i in range(4):
            nr = bar_x + dr[i]
            nc = bar_y + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc]=='0':
                return True
        return False
    return False


def bfs():
    global N,M,visited,arr,res,initial_loc_x, initial_loc_y,bar_x,bar_y,Q

    while Q:
        r, c, d = Q.popleft()
        for i in range(4):
            nr=int(r)+dr[i]
            nc=int(c)+dc[i]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and arr[nr][nc]!='#':
                Q.append((nr,nc,d+1))
                arr[nr][nc]='#'
                visited[nr][nc]=1

            if dfs(initial_loc_x-1, initial_loc_y-1) and check(bar_x,bar_y):
                res=d+1
                return res

    return -1

#########################################################

def main():
    global N, M, visited, arr, res, initial_loc_x, initial_loc_y, bar_x, bar_y,Q

    N,M=map(int,read().split())
    initial_loc_x, initial_loc_y, bar_x,bar_y=map(int,read().split())
    arr=[]
    visited=[[0 for _ in range(M)] for _ in range(N)]
    Q=deque()

    for i in range(N):
        arr.append(list(read().rstrip()))

    Q.append((initial_loc_x-1, initial_loc_y-1,0))
    arr[initial_loc_x-1][initial_loc_y-1]='#'

    print(bfs())

if __name__=='__main__':
    main()
