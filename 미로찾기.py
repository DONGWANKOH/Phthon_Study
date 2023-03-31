# 4 6
# 101111
# 101010
# 101011
# 111011

import sys
from collections import deque
read=sys.stdin.readline

# matrix=[[0 for _ in range(M)] for _ in range(N)]

dr=[-1,1,0,0]  #밖에 따로 관리하는 것이 좋다. 전역변수 개념이기 때문에.
dc=[0,0,-1,1]

N,M=map(int,read().rstrip().split())
visited=[[0 for _ in range(M)] for _ in range(N)]
matrix=[]

for i in range(N):
    matrix.append(list(map(int,read().rstrip()))) #rstrip을 안 쓰면 엔터의 /n 도 다 들어가진다.

def bfs(N,M):
    Q=deque()
    Q.append((0,0))
    visited[0][0]=1
    while Q:
        r=Q[0][0]
        c=Q[0][1]
        Q.popleft()
        if r == N - 1 and c == M - 1:  #밖이다. visited[nr][nc]를 업데이트하고 break 되야한다.
            break
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if 0<=nr<N and 0<=nc<M and matrix[nr][nc]==1 and visited[nr][nc]==0: # if 에서도 순서가 중요하다.. 배열을 쓰는 list를 쓰는 변수로 index Error가 많이 날 꺼다..
                Q.append((nr,nc))
                visited[nr][nc]=visited[r][c]+1
        # print(visited)
    return visited[N-1][M-1]

print(bfs(N,M))

##정답코드 ###########
#
# import sys
# from collections import deque
# read = sys.stdin.readline
#
# global R, C, a, visited
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def bfs():
#     global R, C, a, visited
#     # 큐 선언 및 시작점 표시
#     Q = deque([(0, 0)])
#     # visited 시작점 표시
#     visited[0][0] = 1
#
#     while len(Q):
#         r, c = Q.popleft()
#
#         if r == R - 1 and c == C - 1:
#             break
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             # 맵 위치 벗어나는 경우 무시
#             if nr < 0 or nr >= R or nc < 0 or nc >= C:
#                 continue
#             # 방문한 적 있으면 무시
#             if visited[nr][nc] != 0:
#                 continue
#             # 문제 조건. 1인 곳만 이동할 수 있음
#             if a[nr][nc] != 1:
#                 continue
#             # 다음에 이동할 좌표 저장
#             Q.append((nr, nc))
#             # visited에 지금까지 걸린 횟수 저장. 다른 문제에서는 1로 체크하면 됨
#             visited[nr][nc] = visited[r][c] + 1
#
#
# def main():
#     global R, C, a, visited
#     R, C = map(int, read().rstrip().split())
#
#     visited = [[0 for _ in range(C)] for _ in range(R)]
#     a = []
#
#     for i in range(R):
#         row = list(map(int, read().rstrip()))
#         a.append(row)
#
#     bfs()
#     print(visited[R - 1][C - 1])
#
# if __name__ == '__main__':
#     main()
