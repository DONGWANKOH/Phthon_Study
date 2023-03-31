import sys
from collections import deque
read = sys.stdin.readline

global R, C, visited, a, Q, cnt
res = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global cnt, res
    while len(Q) > 0:
        r, c, d = Q.popleft()   #r=Q[0][0],  c=Q[0][1], d=Q[0][2] Q.popleft()로 반환

        for i in range(4):  #상하좌우로 반복
            nr = r + dr[i]
            nc = c + dc[i]

            # 맵 범위 벗어나거나 방문 했거나 정상 생쥐 아닌 경우
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or a[nr][nc] != 0:
                continue                                                         #-1로 막혀 있는 경우
                                                                                       0 -1
                                                                                       -1 1

            Q.append((nr, nc, d + 1))   #d+1은 다음날 감염 되는 것을 반영
            visited[nr][nc] = 1
            a[nr][nc] = 1  #감염으로 표시하는 식

            cnt -= 1
            if cnt == 0:
                res = d + 1
                return



def main():
    global R, C, visited, a, Q, cnt  #a는 matrix 저장
    C, R = map(int, read().rstrip().split())   #main함수 안에 입력하게 반영함. 몇 마리의 쥐가 감염된지 모르기때문

    a = []
    visited = [[0 for c in range(C)] for r in range(R)]
    Q = deque()
    cnt = 0

    for i in range(R):
        c = list(map(int, read().split()))
        a.append(c)
        for j in range(C):
            # 감염된 쥐 미리 큐에 저장
            if a[i][j] == 1:
                Q.append((i, j, 0))   #0는 처음을 의미함 나중에 +1 +1 되는 부분
                visited[i][j] = 1
            elif a[i][j] == 0:
                cnt += 1
    bfs()

    if cnt == 0:
        print(res)
    else:
        print(-1)


if __name__ == '__main__':
    main()