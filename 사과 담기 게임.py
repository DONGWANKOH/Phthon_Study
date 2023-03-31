# import sys
# # sys.setrecursionlimit(10**9)
# read=sys.stdin.readline
#
#
# N,M=map(int,read().split())
# K=int(read().rstrip())
# a=[]
# ans=0
#
#
# for i in range(K):
#     a.append(int(read().rstrip()))
#
# for j in range(len(a)-1):
#     ans+=abs(a[j+1]-a[j])-(M-1)
#
# print(ans)


import sys
read = sys.stdin.readline


def main():
    N, M = map(int, read().rstrip().split())
    J = int(read().rstrip())
    a = []

    for _ in range(J):
        a.append(int(read().rstrip()))

    # 수레는 처음 왼쪽에 M 칸을 차지하고 있음
    # 길이가 아니고 칸 단위임
    # 1칸부터 M칸까지 M개의 칸을 차지한다는 개념으로 접근
    l = 1   # 수레가 차지하고 있는 가장 왼쪽 칸
    r = M   # 수레가 차지하고 있는 가장 오른쪽 칸
    res = 0

    for apple in a:
        if apple < l:  # 사과가 수레 왼쪽에 떨어지는 경우
            move = l - apple
            l = apple   # 사과가 떨어지는 위치에 왼쪽 칸을 맞춤
            r -= move   # 수레가 움직이니까 오른쪽 위치도 수정
            res += move    # 이동한 거리 갱신
        elif apple > r: # 사과가 수레 오른쪽에 떨어지는 경우
            move = apple - r
            r = apple   # 사과가 떨어지는 위치에 오른쪽 칸을 맞춤
            l += move   # 수레가 움직이니까 왼쪽 위치도 수정
            res += move     # 이동한 거리 갱신

    print(res)


if __name__ == '__main__':
    main()




    # ans-=M-1

##문제 잘못 이해한 경우
# a.append(int(read().rstrip()))
#
# while True:
#     a.append(int(read().rstrip()))
#     if a[-1]==a[0]:
#         break
#     # print(a)
# a.pop()
# # print(a)
#
# for j in range(0,len(a)-1):
#     ans+=abs(a[j+1]-a[j])-(M-1)
#     # print(ans)
#     # ans-=M-1
# print(ans)