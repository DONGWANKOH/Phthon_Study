import sys
from collections import deque
sys.setrecursionlimit(10**9)
read=sys.stdin.readline


def war():
    global N, H_atk, H_max, H_cur,room

    t,a,h=room.popleft()
    if t==1:
        while h>0 and H_cur<=0:   #용사의 공격력 : 1 <<<<<<<<<<<<<< 몬스터의 체력 : 1,000,000
            h-=H_atk
            if h>0: #몬스터가 먼저 죽고나면 용사를 공격 못 한다. 이 점 주의하여 삽입함...
                H_cur-=a
        return H_cur

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
    # print(H_cur)
    # print(min(ans))
    print(max(-1*H_cur+1,-(min(ans)-1)))


if __name__=='__main__':
    main()