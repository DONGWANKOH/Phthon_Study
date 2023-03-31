import sys
read=sys.stdin.readline

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dfs(r,c):
    global visited,N,M,arr,num
    visited[r][c]=1
    arr[r][c] =num
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc]==0 and visited[nr][nc]==0:
            dfs(nr,nc)

def hole_check():  #hole을 만났는지 여부, 만났으면 hole도 연결할 필요


def main():
    global visited, N,M, arr,num
    N,M=map(int,read().split())
    visited=[[0 for _ in range(M)] for _ in range(N)]

    arr=[]
    for i in range(N):
        arr.append(list(map(int,read().split())))

    num = -1
    for i in range(N):
        for j in range(M):
            # if (a[i][j-1]==0 and a[i][j]==1 and visited[i][j]==0) or (a[i][j]==0 and a[i][j]==1 and visited[i][j]==0):
            if arr[i][j]==0 and visited[i][j]==0:
                dfs(i,j)
                num-=1

    visited = [[0 for _ in range(M)] for _ in range(N)]
    res_1=2
    ######테두리 한 줄을 0으로 녹인다.
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 1 and arr[i-1][j] == -1 ) or (arr[i][j] == 1 and arr[i][j-1] == -1) or (arr[i][j] == 1 and arr[i+1][j] == -1 ) or (arr[i][j] == 1 and arr[i][j+1] == -1):
                arr[i][j]=res_1
                if arr[i][j]
    res_2=res_1+1
  ############# a[i][j] <-1 부분들은 구멍이다...
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 1 and arr[i-1][j] == res_1 ) or (arr[i][j] == 1 and arr[i][j-1] == res_1) or (arr[i][j] == 1 and arr[i+1][j] == res_1 ) or (arr[i][j] == 1 and arr[i][j+1] == res_1):
                arr[i][j]=res_2

    res_3 = res_2 + 1
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 1 and arr[i-1][j] == res_2 ) or (arr[i][j] == 1 and arr[i][j-1] == res_2) or (arr[i][j] == 1 and arr[i+1][j] == res_2) or (arr[i][j] == 1 and arr[i][j+1] == res_2):
                arr[i][j]=res_3

    # for i in range(N):
    #     for j in range(M):


    ###########출력#####################
    for i in range(N):
        for j in range(M):
            print('%2d' %arr[i][j], end=' ')
        print()

    print('------------------------------')

if __name__=='__main__':
    main()