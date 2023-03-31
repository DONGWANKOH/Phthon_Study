from bisect import*
import sys
read=sys.stdin.readline
#첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며,
# 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000)

T=int(input())

while T>0:
    C = 0
    D = []
    N, M = map(int, read().split())
    A=list(map(int,read().rstrip().split()))
    B=list(map(int,read().rstrip().split()))
    A.sort()
    B.sort()
    # print(A)
    # print(B)
    for i in A:
        if bisect_left(B,i)>0: D.append(bisect_left(B,i))
    T-=1
    print(sum(D))


