# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.readline
global b

N,M,K=map(int,read().split())
area=[]
matrix=[[0 for _ in range(M)] for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]

dr=[-1,1,0,0]
dc=[0,0,-1,1]
res=0

ans=[]

for i in range(K):
    x_min,y_min,x_max,y_max=map(int,read().split())
    area.append((x_min,y_min,x_max,y_max))
# print(area)


#좌표 받아서 모두 1로 바꾸기
for p in area:  #대칭이기 때문에 좌표가 반대여도 상관없다
    # print(p[0],p[1],p[2],p[3])
    for i in range(p[1],p[3]):
        for j in range(p[0],p[2]):
            matrix[i][j]=1

# print(matrix)
def dfs(r,c):
    global b
    visited[r][c]=1

    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<M and matrix[nr][nc]==0 and visited[nr][nc]==0:
            dfs(nr,nc)
            b += 1
    return b


for i in range(N):
    for j in range(M):
        if matrix[i][j]==0 and visited[i][j]==0:
            b = 1
            ans.append(dfs(i,j))

print(len(ans))
ans.sort()
print(*ans)