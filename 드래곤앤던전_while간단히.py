import sys
from collections import deque
read=sys.stdin.readline


def war():
    global N, H_atk, H_max, H_cur, room

    t, a, h = room.popleft()
    if t == 1:
        while h > 0 and H_cur > 0:  # 몬스터가 죽거나 용사가 죽을 때까지 싸웁니다.
            h -= H_atk
            if h > 0:  # 몬스터가 아직 살아있으면, 몬스터가 용사를 공격합니다.
                H_cur -= a
        return H_cur

    elif t == 2:
        H_atk += a
        H_cur = min(H_cur + h, H_max)
        return H_cur


def main():
    global N,H_atk, H_max, H_cur,room
    N, H_atk=map(int,read().split())
    room = deque()
    H_max=0
    H_cur=0
    for i in range(N):
        t,a,h=map(int,read().split())
        room.append((t,a,h))
    # print(room)

    for i in range(N):
        war()
    # print(H_cur)
    print(-1*H_cur+1)


if __name__=='__main__':
    main()