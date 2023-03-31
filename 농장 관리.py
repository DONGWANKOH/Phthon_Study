
import sys
read=sys.stdin.readline
global N,M,a,visited,res

dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]

def dfs(r,c):
    visited[r][c]=1
    for i in range(8):
        nr=r+dr[i]
        nc=c+dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=M or a[nr][nc]<=a[r][c] or visited[nr][nc] !=0:
            continue

        # elif a[nr][nc]>=a[r][c]:
        #     return
        dfs(nr,nc)

def main():
    global N,M,a,visited,res

    N,M=map(int,read().rstrip().split())
    a=[]
    res=0
    visited=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        a.append(list(map(int, read().split())))

    for i in range(N+1):
        for j in range(M+1):
            if a[i+1][j+1]>a[i][j] and visited[i][j]==0:
                dfs(i,j)
                res+=1
    print(res)

if __name__=='__main__':
    main()