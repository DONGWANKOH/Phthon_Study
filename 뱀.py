import sys
from collections import deque

read=sys.stdin.readline

dir=[(1,0),(0,1),(-1,0),(0,-1)]  #이동 좌표계

# def apple(r,c): #사과 개수 업데이트
#뱀이 존재하는 matrix 추가 자리, Bam matrix를 1로 표현한다.

def move(r,c):
    global cnt,N,rotate_dir,matrix,l,Bam
    k=0
    Q.append((r,c))
    while Q:
        r,c=Q.popleft()

        if Q:
            Q.popleft()  #꼬리 부분 삭제########

        if r<0 or r>=N or c<0 or c>=N:
            return cnt

        if (r,c) in Q: #Q안에 들어있는 모든 뱀의 좌표를 만나면
            return cnt

        for p in rotate_dir:
            if cnt==p[0]:
                if p[1]=='D':
                    k=(k+1)%4
                elif p[1]=='L':
                    k=(k-1)%4
        nr=r+dir[k][0]
        nc=c+dir[k][1]

        if matrix[nr-1][nc-1]==1:  #사과를 먹으면 뱀의 길이가 늘어나야한다..........
            Q.appendleft((nr,nc))

        if nr<0 or nr>=N or nc<0 or nc>=N: #bam==1:
            return cnt
        cnt+=1
        Q.append((nr,nc))


def main():
    global cnt,Q,rotate_dir,N,matrix,l,Bam
    Q=deque()

    N=int(read())
    K=int(read())
    matrix=[[0 for _ in range(N)] for _ in range((N))]
    Bam = [[0 for _ in range(N)] for _ in range((N))]
    rotate_dir=[]
    cnt=0
    l=1

    for i in range(K):
        a,b=map(int,read().split())
        matrix[a-1][b-1]=1

    P = int(read())
    for i in range(P):
        a,b=read().split()
        a=int(a)
        rotate_dir.append([a,b])

    move(0,0)

    print(cnt+1)
if __name__=='__main__':
    main()