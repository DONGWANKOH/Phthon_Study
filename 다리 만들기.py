import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 섬을 구분해주는 bfs
def bfs1(r, c):
    global count
    Q = deque()
    Q.append([r, c])
    vis[r][c] = 1
    arr[r][c] = count

    while len(Q)>0:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1 and vis[nr][nc]==0:
                vis[nr][nc] = 1
                arr[nr][nc] = count
                Q.append([nr, nc])

# 바다를 건너며 가장 짧은 거리를 구한다.
def bfs2(z):
    global answer
    dist = [[-1] * n for _ in range(n)] # 거리가 저장될 배열
    Q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == z:
                Q.append([i, j])
                dist[i][j] = 0

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 갈 수 없는 곳이면 continue
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if arr[nr][nc] > 0 and arr[nr][nc] != z:
                answer = min(answer, dist[r][c])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if arr[nr][nc] == 0 and arr[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                Q.append([nr, nc])


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j] == 1:
            bfs1(i, j)
            count += 1

# print(arr)

for i in range(1, count):
    bfs2(i)

print(answer)