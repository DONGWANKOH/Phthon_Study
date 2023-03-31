import sys
read=sys.stdin.readline



def bfs():
    global res,cnt

    while Q:
        r,c,d=Q.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C or visited[nr][nc]!=0 or a[nr][nc]!=0:
                continue
            Q.append((nr,nc,d+1))
            a[nr][nc]=1
            visited[nr][nc]=1
            cnt-=1
            if cnt==0:
                return res=d+1


def main():

    for r in range(R):
        a,append(list(map(int,read().split())))
        for c in range(C):
            if a[r][c]==1:
                Q.append((nr,nc,0))
                visited[r][c]=1
            elif a[r][c]==0:
                cnt=+1

    bfs()

    if cnt==0:
        print(res)
    else:
        print(-1)