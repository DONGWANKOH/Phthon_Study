# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# 0 0 0 0 1 0
# 1 0 0 1 0 2
# 1 1 1 0 0 2
# 0 0 0 1 0 2 9개

# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0

# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 1 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 #3개

import sys
from itertools import*
# from collections import deque
read=sys.stdin.readline

dr=[-1,1,0,0]
dc=[0,0,-1,1]


def dfs(r,c):
    global visited,matrix,N,M

    matrix[r][c]=2
    visited[r][c]=1
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=M or visited[nr][nc]==1 or matrix[nr][nc]==2 or matrix[nr][nc]==1:
            continue
        dfs(nr,nc)

def main():
    global visited, matrix, N, M

    # Q=deque()
    N,M=map(int,read().split())
    matrix=[]

    visited=[[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):  #matrix를 받고
        matrix.append(list(map(int,read().split())))

    pillar=[]
    virus=[]
    for o in range(N):
        for p in range(M):
            if matrix[o][p]==2: #바이러스가 있는 좌표는 Q로 추가한다.
                virus.append((o,p))
            elif matrix[o][p]==0:  #pillar를 세울 수 있는 부분 : matrix가 0인 부분을 pilar list에 좌표 저장한다.
                pillar.append((o,p))

    # B = copy.deepcopy(A)  A를 B에 복사해서 넣으면 B는 그 이후에 변경되지 않는다.

    for a in combinations(pillar, 3):
        for b in a:
            matrix[b[0]][b[1]]=1
        for x in range(N):
            for y in range(M):
                if matrix[x][y] == 2 and visited[x][y] == 0:
                    dfs((x, y))


if __name__ == '__main__':
    main()


#######################################정답################################################

from collections import deque
import sys
from copy import *
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

global R, C, a, visited, virus, blank, res
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def count_safe():
    global R, C, a, visited, virus, blank, res
    cnt = 0
    for i in range(R):
        for j in range(C):
            # 빈칸이고 방문한 적 없으면 안전지대
            if a[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    res = max(cnt, res)


def bfs(Q):
    global R, C, a, visited, virus, blank, res
    # 벽 세우는 곳 달라질때마다 초기화 해야 되므로 여기서 해야 됨
    visited = [[0 for _ in range(C)] for _ in range(R)]

    for r, c in virus:
        visited[r][c] = 1

    while len(Q) > 0:
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 맵 범위 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            # 방문 체크
            if visited[nr][nc] != 0:
                continue
            # 빈칸(0)으로만 퍼질 수 있음
            if a[nr][nc] != 0:
                continue
            # 큐에 넣고 visited 체크. 맵은 변화 시키면 안됨(재활용 하기 위해서)
            Q.append((nr, nc))
            visited[nr][nc] = 1


def main():
    global R, C, a, visited, virus, blank, res
    R, C = map(int, read().rstrip().split())
    a = []
    virus = deque()
    blank = []
    res = 0

    for i in range(R):
        c = list(map(int, read().rstrip().split()))
        a.append(c)
        for j in range(C):
            if a[i][j] == 2:    # 바이러스 위치 저장
                virus.append((i, j))
            if a[i][j] == 0:    # 빈 공간 위치 저장. 벽이 놓일 후보 리스트
                blank.append((i, j))

    for i in range(len(blank) - 2):     # 벽 선택
        a[blank[i][0]][blank[i][1]] = 1

        for j in range(i + 1, len(blank) - 1):  # i 다음 인덱스부터 벽 하나 선택
            a[blank[j][0]][blank[j][1]] = 1

            for k in range(j + 1, len(blank)):  # j 다음 인덱스부터 벽 하나 선택
                a[blank[k][0]][blank[k][1]] = 1
                bfs(deepcopy(virus))   # 바이러스가 담긴 큐에 내용물이 변하는 것을 막기 위해 deepcopy로 복사본 보냄
                count_safe()
                a[blank[k][0]][blank[k][1]] = 0     # 현재 벽 해제

            a[blank[j][0]][blank[j][1]] = 0     # 현재 벽 해제

        a[blank[i][0]][blank[i][1]] = 0     # 현재 벽 해제

    print(res)

if __name__ == '__main__':
    main()



#####################chat GPT###### 및 내 코드 수정######################################

import sys
from itertools import combinations   # 수정1: combinations 모듈만 import
read = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, visited, matrix):    # 수정2: visited, matrix 파라미터로 전달
    matrix[r][c] = 2
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]) or visited[nr][nc] == 1 or matrix[nr][nc] == 2 or matrix[nr][nc] == 1:
            continue
        dfs(nr, nc, visited, matrix)


def main():
    N, M = map(int, read().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, read().split())))

    pillar = []
    virus = []
    for o in range(N):
        for p in range(M):
            if matrix[o][p] == 2:
                virus.append((o, p))
            elif matrix[o][p] == 0:
                pillar.append((o, p))

    max_safety_zone = 0   # 수정3: 안전 구역의 최대 크기를 구하기 위한 변수 추가
    for a in combinations(pillar, 3):
        temp_matrix = [row[:] for row in matrix]   # 수정4: matrix의 원래 값을 바꾸지 않기 위해 temp_matrix 생성

        for b in a:
            temp_matrix[b[0]][b[1]] = 1
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for x, y in virus:
            dfs(x, y, visited, temp_matrix)
        count = sum(row.count(0) for row in temp_matrix)  # 수정5: 안전 구역 크기를 계산
        max_safety_zone = max(max_safety_zone, count)  # 수정6: 최대 안전 구역 크기 업데이트

    print(max_safety_zone)  # 수정7: 최대 안전 구역 크기 출력


if __name__ == '__main__':
    main()

