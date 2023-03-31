from collections import deque
import sys
from itertools import permutations
read = sys.stdin.readline

global C, R, a, visited, dist, pos, S, E, res

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start, end, num):   # 출발점 좌표, 목표지점 좌표, 도착지점의 숫자
    global C, R, a, visited, dist, pos, S, E, res
    start_r, start_c = start
    end_r, end_c = end

    Q = deque([(start_r, start_c, 0)])  # r, c, 걸음 수
    visited[start_r][start_c] = num   # visited를 여러번 초기화 하지 않기 위해 visited에 방문 표시 변수를 목표 지점의 숫자로 잡음

    while len(Q) > 0:
        r, c, step = Q.popleft()

        if r == end_r and c == end_c:   # 도착지점 왔으면 걸음 수 return
            return step

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            # 방문 체크
            if visited[nr][nc] == num:
                continue
            # 벽이면 무시
            if a[nr][nc] == '#':
                continue

            Q.append((nr, nc, step + 1))
            visited[nr][nc] = num


def Solve(seq):
    global C, R, a, visited, dist, pos, S, E, res
    visited = [[0 for _ in range(C)] for _ in range(R)]

    sum = 0

    for i in range(1, len(seq)):
        # 지도에 매겨놓은 번호 이용하여 start랑 end 번호 가져오기
        r, c = seq[i - 1]
        start = a[r][c]
        nr, nc = seq[i]
        end = a[nr][nc]

        if dist[start][end] == 0:   # 기존에 저장된 값이 없으면 bfs로 거리 구하기
            dist[start][end] += bfs(seq[i - 1], seq[i], end)
            dist[end][start] = dist[start][end]

        sum += dist[start][end]

        if sum >= res:  # 가지치기. 지금까지 값이 이미 res 이상이면 굳이 뒤에 할 필요 없음
            return

    res = min(res, sum)


def main():
    global C, R, a, visited, dist, pos, S, E, res
    C, R = map(int, read().rstrip().split())
    visited = [[0 for _ in range(C)] for _ in range(R)]
    a = []  # 지도
    pos = []    # 물건 위치
    res = int(1e9)  # 최솟값 구하는 문제 이므로 최댓값 저장

    for i in range(R):
        c = list(map(str, read().rstrip()))
        a.append(c)
        for j in range(C):
            if a[i][j] == 'S':  # 시작점 저장
                S = (i, j)
            elif a[i][j] == 'E':    # 끝점 저장
                E = (i, j)
            elif a[i][j] == 'X':    # 물건 위치 저장
                pos.append((i, j))

    # 지도에 이동해야 되는 위치들 값 변경 하기
    a[S[0]][S[1]] = 0   # 시작점 0으로 변경
    a[E[0]][E[1]] = len(pos) + 1    # 끝점은 물건 개수로 변경
    # 물건들 순서대로 map에 번호 매기기
    for i in range(len(pos)):
        r, c = pos[i]
        a[r][c] = i + 1

    # 최단 거리 테이블
    dist = [[0 for _ in range(len(pos) + 2)] for _ in range(len(pos) + 2)]

    for permu in permutations(pos):
        # 뽑아낸 순열 원소 앞뒤에 시작점 끝점 붙여서 리스트로 만들기
        seq = []
        seq.append(S)
        seq += list(permu)
        seq.append(E)
        # 뽑아낸 순열 계산
        Solve(seq)

    print(res)


if __name__ == '__main__':
    main()