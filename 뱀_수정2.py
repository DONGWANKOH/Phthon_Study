import sys
from collections import deque

read = sys.stdin.readline

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def move(r, c):
    global cnt, N, rotate_dir, matrix, l, Bam, Q
    k = 0
    Q.append((r, c))

    while Q:
        r, c = Q.popleft()

        if Q:
            tr, tc = Q[-1]
            if not Bam[tr][tc]:
                Q.pop()

        if r < 0 or r >= N or c < 0 or c >= N:
            return cnt

        if (r, c) in Q or Bam[r][c]:
            return cnt

        for p in rotate_dir:
            if cnt == p[0]:
                if p[1] == 'D':
                    k = (k + 1) % 4
                elif p[1] == 'L':
                    k = (k +3) % 4

        nr = r + dir[k][0]
        nc = c + dir[k][1]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            return cnt

        if matrix[nr][nc] == 1:
            matrix[nr][nc] = 0
            l += 1

        cnt += 1
        Q.append((nr, nc))
        Bam[nr][nc] = 1

    return cnt

def main():
    global cnt, Q, rotate_dir, N, matrix, l, Bam
    Q = deque()

    N = int(read())
    K = int(read())
    matrix = [[0] * N for _ in range(N)]
    Bam = [[0] * N for _ in range(N)]
    rotate_dir = []
    cnt = 0
    l = 0

    for i in range(K):
        a, b = map(int, read().split())
        matrix[a - 1][b - 1] = 1

    P = int(read())
    for i in range(P):
        a, b = read().split()
        a = int(a)
        rotate_dir.append([a, b])

    print(move(0, 0) + 1)

if __name__ == '__main__':
    main()
