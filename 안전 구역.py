
import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**9)
matrix=[]

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c,a,visited):

    visited[r][c]=1
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<N and matrix[nr][nc]>a and visited[nr][nc]==0:
            dfs(nr,nc,a,visited)

def main():
    global N, matrix

    N=int(read())
    res=0


    for i in range(N):
        ans=list(map(int,read().split()))
        res=max([*ans,res])  #이 부분이 되는 이유를 명확하게 알 것
        matrix.append(ans)

    ans=[]

    for i in range(res,-1,-1):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        res = 0
        # print(i)
        for o in range(N):
            for p in range(N):
                if matrix[o][p] > i and visited[o][p]==0:
                    # print('진입')
                    dfs(o,p,i,visited)
                    res+=1
        ans.append(res)
    # print(ans)
    if max(ans)==0:
        print(1)
    else:
        print(max(ans))



if __name__=='__main__':
    main()

#######정답##################