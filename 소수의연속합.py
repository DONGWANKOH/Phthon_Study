from math import sqrt
import sys

read = sys.stdin.readline


def main():
    N = int(read().rstrip())
    composite = [False for _ in range(N + 1)]   # 소수 판별을 위해 합성수를 걸러낼 배열. True면 소수가 아님

    # 에라토스테네스의 체
    for i in range(2, int(sqrt(N)) + 1):
        if composite[i]:    # True. 즉 소수가 아닌 경우. i가 이미 걸러졌으면 i의 배수 또한 이미 걸러져있음
            continue
        for j in range(i * 2, N + 1, i):
            composite[j] = True     # 합성수 표시. 즉 소수가 아님을 표시

    # print(composite)


    prime = []  # 소수만 저장할 리스트

    for i in range(2, N + 1):
        if not composite[i]:    # False인 경우.
            prime.append(i)

    lo = hi = sum = res = 0     # 필요한 변수들 전부 0으로 초기화

    # 투포인터
    while True:
        # if len(prime) == hi:
        #     break

        if sum > N:     # 합이 더 큰 경우.
            sum -= prime[lo]    # 지금까지 더한 값 중 가장 작은 값을 빼줌
            lo += 1     # 가장 작은 값의 인덱스를 의미하던 lo를 오른쪽으로 한 칸 이동

        # 위의 if에서 lo가 이동하는 경우는 이미 다 가려냄. 이제는 hi가 이동하는 경우 밖에 없음
        # hi가 이동하기 전에 hi가 이미 prime의 마지막을 가리키면 종료 시킴.
        # 이 조건이 먼저 나오지 않으면 인덱스 에러 발생함
        elif len(prime) == hi:
            break
        elif sum <= N:      # 합이 작거나 같은 경우. 다음 값을 더해줌. 같은 경우도 이제 답이 되었으니 다음 연산을 보기 위함
            sum += prime[hi]
            hi += 1
        # 위의 작업에서 N값을 만들어 냈으면 경우의 수 하나 추가
        if sum == N:
            res += 1

    print(res)


if __name__ == '__main__':
    main()

