# 4 7
# 20 15 10 17
#이분 탐색은 무엇을 구해야하는지 확인해야한다.
# M보다 큰 값들 중의 최솟값을
import sys
read = sys.stdin.readline
global N, M, a, res

def check(mid):
    global N, M, a, res
    sum = 0

    for i in a:
        # 절단기 높이가 더 높으면 나무가 안잘림. 음수값이 나와 잘못된 결과 도출
        if mid >= i:
            continue
        sum += i - mid

    # 자른 길이는 M은 되어야 함
    return sum >= M


def main():
    global N, M, a, res
    N, M = map(int, read().rstrip().split())
    a = list(map(int, read().rstrip().split()))

    lo = 0
    hi = max(a) # 나무 최대 높이를 기준으로 잡으면 하나도 안잘리기 때문에 기준으로 잡음

    while lo <= hi:
        # 절단기의 높이.
        mid = (lo + hi) // 2

        # 길이가 M 만큼 확보 된 경우. 우리는 이 중에 최소값을 원함. 최소가 되려면 절단기 높이가 최대가 되어야 함
        if check(mid):
            lo = mid + 1
            res = mid
        else:   # 길이가 M 만큼 확보 안된 경우. 더 많이 자르려면 높이를 낮춰야 됨.

            hi = mid - 1

    # print(lo,hi)
    print(res)


if __name__ == '__main__':
    main()

####################################
# import sys
# read = sys.stdin.readline
#
# N, M = map(int, read().rstrip().split())
# tree = list(map(int, read().rstrip().split()))
#
# l = min(tree)
# h = max(tree)
# t = (l + h) // 2
# # res = 0
# sum_tree=0
# ans=[]
# while sum_tree < M:
#     print(sum_tree,tree,t)
#     for i in tree:
#         if i - t >= 0:  #max(0,h-t) 바로 시간 초과..발생한다..
#             sum_tree += (i-t)
#     ans.append(sum_tree)
#     if sum_tree >= M:
#         break
#         # sum_tree = 0
#         # h = h - t / 2
#
#     elif sum_tree < M:
#         sum_tree = 0
#         t = l + t// 2
#     # elif
#     # print(sum_tree)
#         # else:
#         #     res = sum_tree
#     # if sum_tree==M:
#     #     break
# print(min(sum_tree),t)




##########
# import sys
# read=sys.stdin.readline
# N,M=map(int,read().split())
# T=list(map(int,read().split()))
# # T_cut=[]
# ans=0
# # print(max(T))
#
# for j in range(max(T),0,-1):
#     T_cut = []
#     for i in T:
#         if i>=j:
#             T_cut.append(i-j)
#             # print(i,T_cut)
#     if sum(T_cut)>=M:
#         ans=j
#         break
#
# print(ans)


'''시간초과############################################
import sys
read=sys.stdin.readline
N,M=map(int,read().split())
T=list(map(int,read().split()))
# T_cut=[]
ans=0
# print(max(T))

for j in range(max(T),0,-1):
    T_cut = []
    for i in T:
        if i>=j:
            T_cut.append(i-j)
            # print(i,T_cut)
    if sum(T_cut)>=M:
        ans=j
        break

print(ans)
'''
