import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**5)  ###붙이고 시작하기....

###########수동으로 다 세보자.. reset도 해보고..###################
# 1<=N : map이 0일 수 없음..

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


################################
def dfs1(r, c):
    global visited_G, arr, N
    visited_G[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'G' and visited_G[nr][nc] == 0:
            dfs1(nr, nc)


###################################
def dfs2(r, c):
    global visited_R, arr, N
    visited_R[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'R' and visited_R[nr][nc] == 0:
            dfs2(nr, nc)
        ###########################


def dfs3(r, c):
    global visited_B, arr, N
    visited_B[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'B' and visited_B[nr][nc] == 0:
            dfs3(nr, nc)
        ######################################


def dfs4(r, c):
    global visited_merge, arr, N
    visited_merge[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in 'GR' and visited_merge[nr][nc] == 0:
            dfs4(nr, nc)
        #####################################


def main():
    global visited_G, visited_R, visited_B, visited_merge, arr, N
    N = int(read())
    arr = []
    visited_G = [[0 for _ in range(N)] for _ in range(N)]
    visited_R = [[0 for _ in range(N)] for _ in range(N)]
    visited_B = [[0 for _ in range(N)] for _ in range(N)]
    visited_merge = [[0 for _ in range(N)] for _ in range(N)]
    res_G = 0
    res_R = 0
    res_B = 0
    res_merge = 0

    ans = []
    for i in range(N):
        arr.append(read().strip())

    for p in range(N):
        for q in range(N):
            if arr[p][q] == 'G' and visited_G[p][q] == 0:
                dfs1(p, q)
                res_G += 1
    ans.append(res_G)

    for p in range(N):
        for q in range(N):
            if arr[p][q] == 'R' and visited_R[p][q] == 0:
                dfs2(p, q)
                res_R += 1
    ans.append(res_R)

    for p in range(N):
        for q in range(N):
            if arr[p][q] == 'B' and visited_B[p][q] == 0:
                dfs3(p, q)
                res_B += 1
    ans.append(res_B)

    for p in range(N):
        for q in range(N):
            if arr[p][q] in 'GR' and visited_merge[p][q] == 0:
                dfs4(p, q)
                res_merge += 1
    ans.append(res_merge)
    # print(ans)
    ########G      R     B       B  +merge(GR)
    print(ans[0] + ans[1] + ans[2], ans[2] + ans[3])  # R을 안 세버리면?


if __name__ == '__main__':
    main()