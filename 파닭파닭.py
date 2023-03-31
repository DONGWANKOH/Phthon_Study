import sys

read = sys.stdin.readline


def check(mid):
    global C, a
    sum = 0
    # 파를 mid의 길이로 자르면 몇조각 나오는지 카운팅
    for i in a:
        sum += i // mid

    # 파닭을 C개 만들어야 되기 때문에 C개 이상 있어야 됨
    return sum >= C


def main():
    global C, a
    S, C = map(int, read().rstrip().split())
    a = []

    for _ in range(S):
        a.append(int(read().rstrip()))

    hi = max(a)
    lo = 1
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2

        # 가능한 경우 중 mid값이 최대가 되어야 함
        if check(mid):
            lo = mid + 1
            res = mid
        # 불가능한 경우는 파의 조각 개수가 더 많이 나오게 하기 위해 길이를 짧게 잡아야 됨
        else:
            hi = mid - 1
    # 전체 파의 길이 - 자른 파의 길이 * 파의 개수
    print(sum(a) - res * C)


if __name__ == '__main__':
    main()

'''
    ###########################################

    lo=0
    hi=max(a)
    sum=0

    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]==
'''
