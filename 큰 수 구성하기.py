# #재귀함수에 이해도가 낮다.
# 1, 5, 7
#
# 7 7 7
# 7 5 7 등등
#
# 100,000,000 1억인 경우 for문으로는 막겠다
# 중복순열이라 case 줄이기 위해 K를 1,3사이로주었다.
#                1           5        7
# 0(1의 자리)     1           5        7
# 1(10의 자리) 1  5  7     1  5  7  1  5  7


import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

global a, res, N, K


def recursive(x):
    global a, res, N, K
    if N < x:   # N 보다 작거나 같은 자연수 중 가장 큰 수를 찾는 것이 목적. x가 더 크면 위배
        return
    print('max전:',x)
    # N을 넘는 경우는 이제 없음. 지금까지 나온 수 중 가장 큰 수로 res 갱신
    res = max(res, x)
    print('max후:',res)
    for i in a:  # 1 5 7
        recursive(x * 10 + i)   # 1의 자리에 a 원소 하나 넣어서 위의 작업 반복


def main():
    global a, res, N, K
    N, K = map(int, read().rstrip().split())
    a = list(map(int, read().rstrip().split()))
    res = -1    # 최댓값 구하는 문제. 자연수 구하는 문제이므로 -1보다는 무조건 큼

    recursive(0)
    print(res)


if __name__ == '__main__':
    main()

    ###########################################내가 푼 코드  ---틀림
# import sys
# read=sys.stdin.readline
#
# ans=[]
# res=[]
# res_1=[]
# def Check(n,k,nu):
#     n=list(str(n))
#     print(n)
#     nu.sort()
#     for i in range(len(nu)-1,-1,-1):
#         for j in n:
#             if int(j)>=nu[i]:
#                 ans.append(nu[i])
#             print(ans)
#         res.append(max(ans))
#     # res_1.append(res)
#     print(res)
#
#     return
#
#
# def main():
#
#     N,K=map(int,read().split())
#     num=list(map(int,read().split()))
#     print(Check(N, K, num))
#     # print(Check(N,K,num))
#
#
#
#
# if __name__=='__main__':
#     main()