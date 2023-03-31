import sys

read = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

import sys

read = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global visited, N, M, matrix, cnt
    visited[r][c] = 1
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] == 1 and visited[nr][nc] == 0:
            # cnt+=1
            dfs(nr, nc)

    # return cnt


def main():
    global visited, N, M, matrix, cnt
    N, M, K = map(int, read().split())

    matrix = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    visited = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    res = []
    cnt = 0
    for k in range(K):
        r, c = map(int, read().rstrip().split())
        matrix[r][c] = 1

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                # cnt=1
                dfs(i, j)
                # cnt+=1
                res.append(cnt)

    # print(res)
    print(max(res))


if __name__ == '__main__':
    main()
