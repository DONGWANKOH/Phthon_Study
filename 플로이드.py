import sys
read=sys.stdin.readline

def main():

    INF=987654321
    N=int(read())
    M=int(read())
    arr = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(M):
        a,b,c=map(int,read().split())
        arr[a][b]=min(arr[a][b],c)  #가는 경로가 2개 이상일 때, 최솟값으로 처리하기

    for p in range(N+1):
        arr[p][p]=0

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])

    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j]==INF:  #못 가는 경우 는 0으로 처리하여 출력
                arr[i][j] = 0
                print(arr[i][j],end=' ')
            else:
                print(arr[i][j],end=' ')
        print()
    # print(arr)

if __name__=='__main__':
    main()
