import sys

read = sys.stdin.readline
global C, R, K, visited, a, res

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or a[nr][nc] != 1:
            continue
        dfs(nr, nc)


def main():
    global C, R, K, visited, a, res

    m = int(input())
    N = 0

    while N < m:
        res = 0
        C, R, K = map(int, read().split())
        a = [[0 for c in range(C)] for r in range(R)]
        visited = [[0 for c in range(C)] for r in range(R)]

        for i in range(K):
            c, r = map(int, read().rstrip().split())
            a[r][c] = 1

        for i in range(R):
            for j in range(C):
                if a[i][j] == 1 and visited[i][j] == 0:
                    dfs(i, j)
                    res += 1
        N += 1
        print(res)


if __name__ == '__main__':
    main()




