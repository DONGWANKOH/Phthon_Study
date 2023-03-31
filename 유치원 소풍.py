import sys
read=sys.stdin.readline

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c):
    global n,a,res,size,visited
    visited[r][c]=1
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if nr<0 or nr>=n or nc<0 or nc>=n or a[nr][nc]!=1 or visited[nr][nc] !=0:
            continue

        dfs(nr,nc)
        size+=1
    return size

def main():
    global n,a,res,size,visited
    n=int(input())
    a=[]
    visited=[[0 for _ in range(n)] for _ in range(n)]
    res=[]
    for i in range(n):
        a.append(list(map(int,read().rstrip())))

    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and visited[i][j] ==0:
               size=1
               res.append(dfs(i,j))

    res.sort()
    print(len(res))
    for i in res:
        print(i)

if __name__ == "__main__":
    main()