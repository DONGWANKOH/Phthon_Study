# dir 변수의 이름이 파이썬 내장 함수인 dir()와 겹치지 않도록 바꿔줘야 합니다.
# move() 함수에서 뱀이 이동한 위치를 기록하는 Q 큐에 새로운 위치를 추가할 때,
# Q.append()를 사용하면 뱀의 길이가 늘어나게 됩니다. 따라서 Q.append() 대신에 Q.appendleft()를 사용해서 뱀의 머리를 추가해야 합니다.
# matrix와 Bam 변수를 초기화할 때, 2차원 리스트의 크기를 지정할 때 range() 함수에 괄호를 한 번 더 써주어야 합니다.
# move() 함수에서 뱀이 이동한 위치가 벽이거나 뱀 자신의 몸이 있는 위치인지를 검사할 때,
# 현재 위치가 아니라 다음 위치인 (nr, nc)를 검사해야 합니다.
# 마지막으로 main() 함수에서 rotate_dir 리스트를 입력받을 때, readline()
# 함수로 입력을 받을 때 문자열 마지막의 개행 문자(\n)를 지워주어야 합니다.

import sys
from collections import deque

read = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 이동 좌표계

def move(r, c):
    global cnt, N, rotate_dir, matrix, l, Bam, Q
    k = 0
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()

        if (r, c) in Q:  # Q안에 들어있는 모든 뱀의 좌표를 만나면
            return cnt

        if r < 0 or r >= N or c < 0 or c >= N:  # 벽이면
            return cnt

        if matrix[r][c] == 1:  # 사과를 먹으면 뱀의 길이가 늘어남
            l += 1
            matrix[r][c] = 0

        Q.appendleft((r, c))

        for p in rotate_dir:
            if cnt == p[0]:
                if p[1] == 'D':
                    k = (k + 1) % 4
                elif p[1] == 'L':
                    k = (k - 1) % 4
        nr = r + directions[k][0]
        nc = c + directions[k][1]

        if Bam[nr-1][nc-1] == 1:  # 뱀의 몸통이면
            return cnt

        cnt += 1
        Q.appendleft((nr, nc))
        Bam[nr-1][nc-1] = 1
        Bam[r][c] = 0
        if cnt == rotate_dir[-1][0]:
            rotate_dir.pop()


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