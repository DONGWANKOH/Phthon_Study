import sys
from collections import deque
read=sys.stdin.readline
dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c,num):
    global visited,N,arr
    arr[r][c] = num
    visited[r][c]=1
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==1 and visited[nr][nc]==0:
            dfs(nr,nc,num)
            arr[nr][nc]=num

def bfs():
    global visited, N, arr,Q, ans,num
    r=Q[0][0]
    c=Q[0][1]
    while Q:
        Q.popleft()
        # visited[r][c]=1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]!=0 and arr[nr][nc]!=num :
                ans.append(visited[r][c])
                return

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                Q.append((nr,nc))
                visited[nr][nc]=visited[r][c]+1


            # elif len(Q)==0:
            #     res=visited[r][c]




def main():
    global visited, N, arr,Q,ans,num
    ans=[]
    Q = deque()
    N=int(read())
    arr=[list(map(int,read().strip().split())) for _ in range(N)]
    visited=[[0 for _ in range(N)] for _ in range(N)]
    num=0
    # for i in range(N):
    #     print(arr[i])

    # dfs로 1,2,3으로 arr를 변경하고

    for p in range(N):
        for q in range(N):
            if arr[p][q]==1 and visited[p][q]==0:
                num += 1
                dfs(p,q,num)

    # for i in range(N):
    #     print(arr[i])

    #visited 초기화

    visited = [[0 for _ in range(N)] for _ in range(N)]
    num=1
    for p in range(N):
        for q in range(N):
            if arr[p][q] !=num and visited[p][q]==0:
                visited[p][q]=1
                Q.append((p,q,num))
                bfs()

    print('--------------------------')
    for i in range(N):
        print(visited[i])

    print(ans)
    print('출력',max(ans)*2-1)

    print(max(ans)*2-1)
if __name__=='__main__':
    main()