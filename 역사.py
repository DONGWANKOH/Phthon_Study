import sys
read=sys.stdin.readline


def main():
    n,k=map(int,read().split())
    # stack=[]
    INF=987654321
    arr=[[INF for _ in range(n+1)] for _ in range(n+1)]
    for x in range(n+1):
        for y in range(n+1):
            if x>=y:
                continue
            else:
                arr[x][y] = 1



    for o in range(k+1):
        arr[o][o]=0

    for i in range(k):
        a,b=map(int,read().split())
        arr[a][b]= -1
####################결과값 확인을 위한 곳#########
    # for p in range(k+1):
    #     for q in range(k+1):
    #         # if arr[p][q]==
    #         print(arr[p][q], end=' ')
    #     print()
    # print('---------------------------')
####################################################

    for k in range(1,k+1):
        for i in range(1, k + 1):
            for j in range(1, k + 1):
                # if arr[i][k]+arr[k][j]
                #     arr[i][j]=1

                arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
                # els

#############################################
    for p in range(1,k+1):
        for q in range(1,k+1):
            # if arr[p][q]==
            if arr[p][q]==INF or arr[q][p]==INF:
                arr[p][q]=0
                print(arr[p][q], end=' ')
            # elif arr[q][p]
            elif arr[q][p]==-1:
                arr[q][p]=1
                print(arr[q][p], end=' ')
            elif arr[p][q]==1:
                arr[p][q]=1
                print(arr[p][q], end=' ')
            else:
                print(arr[p][q], end=' ')
            # elif arr[p][q]==1:
            #     print(arr[p][q], end=' ')
        print()

if __name__=='__main__':
    main()