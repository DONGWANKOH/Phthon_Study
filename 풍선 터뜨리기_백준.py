from collections import deque
import sys
read = sys.stdin.readline


def main():
    N = int(read().rstrip())
    a = list(map(int, read().rstrip().split()))
    # 큐에 인덱스 저장.
    # 인덱스와 값 둘다 넣는것이 편하지만 인덱스만 가지고 값 구해보기
    Q = deque([i for i in range(N)])
    print(Q)
    while len(Q) > 0:
        index = Q.popleft()
        value = a[index]    # 이동할 칸
        print(index + 1, end=' ')
        # 현재 풍선은 터졌기 때문에 value - 1만큼만 돌려야 됨. 절댓값 기준
        if value > 0:   # 양수인 경우는 -1만큼 돌려야 됨. 큐에서 빼는 순간 초점이 오른쪽으로 가기 때문. 음수는 해당 없음.
            value -= 1
        # 양수가 오른쪽 음수가 왼쪽을 타겟으로 잡는다는 것은 큐는 방향이 반대로 돌아야 됨.
        # 내가 움직이는 것이 아닌 풍선이 움직이기 때문
        Q.rotate(-value)
        print(Q)


if __name__ == '__main__':
    main()