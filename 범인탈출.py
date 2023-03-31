from collections import deque
global move, N,M,R,C,L
pipe={1: [1,2,3,4], 2: [1,3], 3: [2,4], 4:[1,2], 5:[2,3], 6:[3,4], 7:[1,4]}
direction = {1:[0,-1], 2:[1,0], 3:[0,1], 4:[-1,0]}
pipe_direction = {1: [(0,-1), (1,0), (0,1),(-1,0)], 2: [(0,-1),(0,1)], 3: [ (1,0),(-1,0)], 4:[(0,-1), (1,0)],
                  5:[ (1,0), (0,1)], 6:[ (0,1),(-1,0)], 7:[(0,-1),(-1,0)]}

# print(pipe.keys())
# print(pipe.values())
# 각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
move=1
# for key,value in pipe_direction.items():
#     print(key,value)
# 0 0 5 3 6 0
# 0 0 2 0 2 0
# 3 3 1 3 7 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0


def bfs(R,C):
    global move, N,M,L, matrix, visited,res

    Q=deque()
    Q.append((R,C))
    visited[R][C] = 1
    for _ in range(L):
        r=Q[0][0]
        c=Q[0][1]

        Q.popleft()
        if r==N-1 and c==M-1:
            break
        for key,value in pipe_direction.items():
            if matrix[r][c]==key:
                # print(value)
                for p in value:
                    nr = r+ p[1]
                    nc = c+ p[0]
                    # print(matrix)
                    # print(p,nr,nc)
                    if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and matrix[nr][nc] !=0:
                        Q.append((nr,nc))
                        visited[nr][nc]=visited[r][c]+1
                        res+=visited[nr][nc]
        # print(visited)
        # res+=sum(visited)
        # print(res)

    # return visited
    # return move

def main():
    global move, N,M,L,matrix,visited,res
    N, M, R, C, L = map(int, input().split())

    matrix = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    res=0

    for q in range(N):
        matrix.append(list(map(int,input().rstrip().split())))
    # print(map)

    if matrix[R][C] != 0 and visited[R][C] == 0:
        # visited[R][C]=1
        bfs(R, C)

    # for i in range(R):
    #     for j in range(M):
    #         if matrix[i][j] !=0 and visited[i][j] ==0:
    #             bfs(i,j)
    #
    # print(sum(max(visited)))
    # print(res)
    # for i in range(M):
    #     for j in range(N):
    print(visited)

    # print(visited)

if __name__=='__main__':
    main()

######################################정답
from collections import deque

global a, visited, res, N, M, R, C, L
dr = [-1, 0, 1, 0]  # 상우하좌. 시계방향으로 잡음. 그래야 2를 더했을때 반대방향이 나와서 계산이 쉬움
dc = [0, 1, 0, -1]
pipe = [  # 파이프 번호 별로 상우하좌 이동 가능한 곳을 1로 표시. 0번은 파이프 번호랑 맞추기 위해 비워둠
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]


def bfs():
    global a, visited, res, N, M, R, C, L
    Q = deque([(R, C, 1)])    # (r, c, 시간)
    visited[R][C] = 1

    while len(Q) > 0:
        r, c, time = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 맵 범위 체크
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # 방문 여부 체크
            if visited[nr][nc] != 0:
                continue

            next_pipe_num = a[nr][nc]   # 다음 파이프 번호
            cur_pipe_num = a[r][c]      # 현재 파이프 번호

            # 현재 파이프 번호의 진행방향이 뚫렸는지 체크
            # 다음 파이프에서는 현재의 반대 방향을 봐야됨. 좌 <-> 우 양쪽이 다 뚫려 있어야 이동가능
            # 상 우 하 좌 의 개념이므로 (i + 2) % 2를 하면 반대 방향이 나옴
            if pipe[next_pipe_num][(i + 2) % 4] == 0 or pipe[cur_pipe_num][i] == 0:
                continue

            if time >= L:   # L이 넘어가면 더 이상 확인할 필요 없음
                continue

            res += 1    # 갈 수 있는 곳 하나 더 추가
            visited[nr][nc] = 1
            Q.append((nr, nc, time + 1))


def solve():
    global a, visited, res, N, M, R, C, L
    N, M, R, C, L = map(int, input().split())
    a = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    res = 1     # 멘홀 뚜껑이 있는 위치는 항상 갈 수 있으므로 1로 시작

    for i in range(N):
        c = list(map(int, input().rstrip().split()))
        a.append(c)

    bfs()


def main():
    T = int(input().rstrip())
    for test in range(1, T + 1):
        solve()
        print("#" + str(test), res)


if __name__ == '__main__':
    main()