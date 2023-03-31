import sys
from collections import deque

read = sys.stdin.readline


def main():
    N = int(read().rstrip())
    Q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    res = [i for i in range(10)]

    # 한 자리 수이면 바로 출력하고 종료
    if N < 10:
        print(res[N])
        return

    # 큐가 빌 때까지 계속 반복
    while len(Q) != 0:
        if len(res) >= N + 1:  # 0이 포함되어 있으므로 N번째를 구했으면 길이는 N + 1이 됨
            break

        x = Q.popleft()
        # 1의 자리보다 하나 작은 수 까지만 반복. 그래야 감소하는 수가 됨. 예를 들어 x가 96 이면 0~5까지만 붙을 수 있음
        for i in range(x % 10):
            # x가 96이면 960을 만든 후 i를 1의자리에 붙이면 감수하는 수가 됨.
            Q.append(x * 10 + i)
            res.append(x * 10 + i)

    # 감소하는 수 개수가 N 만큼 안나왔으면 불가능한 경우
    if len(res) < N + 1:
        print(-1)
    else:

        print(res[N])


if __name__ == '__main__':
    main()