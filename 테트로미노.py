import sys
# from collections import deque
read = sys.stdin.readline

dir=[[(1,0),(1,0),(1,0)], [(1,0),(0,1),(-1,0)], [(0,1),(0,1),(1,0)], [(0,1),(1,0),(0,1)], [(1,0),(1,0),(-1,-1)],
     [(-1,0),(-1,0),(-1,0)], [(-1,0),(0,1),(1,0)], [(0,1),(0,1),(-1,0)], [(0,1),(-1,0),(0,1)], [(-1,0),(-1,0),(1,-1)],
     [(1,0),(1,0),(1,0)], [(1,0),(0,-1),(-1,0)], [(0,-1),(0,-1),(1,0)], [(0,-1),(1,0),(0,-1)], [(1,0),(1,0),(-1,1)],
     [(-1,0),(-1,0),(-1,0)], [(-1,0),(0,-1),(1,0)], [(0,-1),(0,-1),(-1,0)], [(0,-1),(-1,0),(0,-1)], [(-1,0),(-1,0),(1,1)],

     [(0,1),(0,1),(0,1)], [(0,1),(1,0),(0,-1)], [(1,0),(1,0),(0,1)], [(1,0),(0,1),(1,0)], [(0,1),(0,1),(-1,-1)],
     [(0,1),(0,1),(0,1)], [(0,1),(1,0),(0,-1)], [(-1,0),(-1,0),(0,1)], [(-1,0),(0,1),(-1,0)], [(0,1),(0,1),(1,-1)],
     [(0,-1),(0,-1),(0,-1)], [(0,-1),(1,0),(0,1)], [(1,0),(1,0),(0,-1)], [(1,0),(0,-1),(1,0)], [(0,-1),(0,-1),(-1,1)],
     [(0,-1),(0,-1),(0,-1)], [(0,-1),(-1,0),(0,1)], [(-1,0),(-1,0),(0,-1)], [(-1,0),(0,-1),(-1,0)], [(0,-1),(0,-1),(1,1)]]

# def rotate():


def dfs(r,c,s):
    global visited,N,M,matrix,ans_1,ans_2,ans
    visited[r][c]=1
    # s+=matrix[r][c]

    for i in dir:
        # print(i)
        for j in i:
            # print(j)
            nr=r+j[0]
            nc=c+j[1]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
                s+=matrix[nr][nc]
                dfs(nr,nc,s)
        ans.append(s)
        s = 0
    ans_1.append(max(ans))
    # print(ans_1)
    # return max(ans_1)

def main():
    global visited,N,M,matrix,ans_1,ans_2,ans
    N,M=map(int,read().split())
    matrix=[]
    visited=[[0 for _ in range(M)] for _ in range(N)]
    ans = []
    ans_1 = []
    ans_2 = []

    for i in range(N):
        matrix.append(list(map(int,read().split())))
    for n in range(N):
        for m in range(M):
            if 0<=n<N and 0<=m<M and visited[n][m]==0:
                dfs(n,m,0)
    print(max(ans_1))
if __name__=='__main__':
    main()