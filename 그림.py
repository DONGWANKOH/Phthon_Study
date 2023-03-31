import sys

read = sys.stdin.readline
global visited, n, a

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = 1
    size = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= r or nc < 0 or nc >= c or a[nr][nc] != 1 or visited[nr][nc] != 0:
            continue
        size += dfs(nr, nc)
    return size


def main():
    global visited, r, c, a
    r, c = map(int, read().rstrip().split())
    a = []
    visited = [[0 for _ in range(c)] for _ in range(r)]
    res = []

    for i in range(r):
        a.append(list(map(int,read().rstrip().split())))

    # print(a)

    for i in range(r):
        for j in range(c):
            if a[i][j] == 1 and visited[i][j] != 1:
                res.append(dfs(i, j))
    print(res)
    res.sort()

    print(len(res))

    for i in res:
        print(i)


if __name__ == "__main__":
    main()


# import sys
# read=sys.stdin.readline
#
# dr=[-1,1,0,0]
# dc=[0,0,-1,1]
#
# def dfs(r,c):
#     visited[r][c]=1
#     size=1
#     for i in range(4):
#         nr=r+dr[i]
#         nc=c+dc[i]
#         if nr<0 or nr>=r or nc<0 or nc>=c or a[nr][nc]!=1 or visited[nr][nc] !=0:
#             continue
#         size+=dfs(nr,nc)
#     return size
#
# def main():
#     global r,c,a,visited
#
#     r, c = map(int, read().rstrip().split())
#     a = []
#     cnt=[]
#     visited=[[0 for _ in range(c)] for _ in range(r)]
#     for i in range(r):
#         a.append(list(map(int, read().rstrip().split())))
#
#     for i in range(r):
#         for j in range(c):
#             if a[i][j]==1 and visited[i][j]==0:
#                 cnt.append(dfs(i,j))
#     print(cnt)
#     # cnt.sort()
#
#     print(len(cnt))
#     print(cnt[-1])
#
# if __name__=='__main__':
#     main()