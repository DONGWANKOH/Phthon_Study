import sys
from collections import deque
sys.setrecursionlimit(10**9)
read=sys.stdin.readline


def war():
    global N, H_atk, H_max, H_cur,room

    t,a,h=room.popleft()
    if t==1:
        q,w=divmod(h,H_atk)
        if w==0:
            H_cur-=a*(q-1)
        else:# q, w = divmod(h, H_atk)
            H_cur-=a*q

    elif t==2:
        H_atk+=a
        H_cur=min(H_cur+h,H_max)  #H_cur 가 0으로 시작함. 싸우고 난 뒤므로 음수,0.. 작은 수로 골라야 한다.

        return H_cur

def main():
    global N,H_atk, H_max, H_cur,room
    N, H_atk=map(int,read().split())
    room = deque()
    H_max=0
    H_cur=0
    ans=[]
    for i in range(N):
        t,a,h=map(int,read().split())
        room.append((t,a,h))
    # print(room)

    for i in range(N):
        war()
        ans.append(H_cur)

    print(max(-1 * H_cur + 1, -(min(ans) - 1)))


if __name__=='__main__':
    main()