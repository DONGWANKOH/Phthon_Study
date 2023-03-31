import sys

read = sys.stdin.readline

dir=[[(1,0),(1,0),(1,0)], [(1,0),(0,1),(-1,0)], [(0,1),(0,1),(1,0)], [(0,1),(1,0),(0,1)], [(1,0),(1,0),(-1,-1)],
     [(-1,0),(-1,0),(-1,0)], [(-1,0),(0,1),(1,0)], [(0,1),(0,1),(-1,0)], [(0,1),(-1,0),(0,1)], [(-1,0),(-1,0),(1,-1)],
     [(1,0),(1,0),(1,0)], [(1,0),(0,-1),(-1,0)], [(0,-1),(0,-1),(1,0)], [(0,-1),(1,0),(0,-1)], [(1,0),(1,0),(-1,1)],
     [(-1,0),(-1,0),(-1,0)], [(-1,0),(0,-1),(1,0)], [(0,-1),(0,-1),(-1,0)], [(0,-1),(-1,0),(0,-1)], [(-1,0),(-1,0),(1,1)]]

def dfs(r,c,s):
    global visited,N,M,matrix
    visited[r][c]=1
    ans_1=[]
    for i in dir:
        ans = []
        for j in i:
            nr=r+j[0]
            nc=c+j[1]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
                ans.append(dfs(nr,nc,s+matrix[nr][nc]))
        if ans:
            ans_1.append(max(ans))
    visited[r][c]=0
    if not ans_1:
        ans_1.append(s)
    return ans_1

def main():
    global visited,N,M,matrix
    N,M=map(int,read().split())
    matrix=[]
    visited=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        matrix.append(list(map(int,read().split())))
    ans = []
    for n in range(N):
        for m in range(M):
            ans += dfs(n,m,matrix[n][m])
    print(max(ans))

if __name__=='__main__':
    main()