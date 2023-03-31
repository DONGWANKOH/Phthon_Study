#입력 : 5
#입력 : 6 9 5 7 4
#출력 : 0 0 2 2 4
#오큰수와 비슷한 유형임

# import sys
# read=sys.stdin.readline
#
#
# def main():
#     N=int(read())
#     top=list(map(int,read().split()))
#     stack=[]
#     ans=[0]
#     # print('top출력',top)
#     # if N==0 or 1:
#     #     print(0)
#     #############################시간 복잡도 O(N^2)
#     for i in range(N):
#         if len(stack)==0:
#             stack.append(top[i])
#         else:
#             while stack and stack[-1] <= top[i]:
#         # else:
#         #     while stack[-1]<=top[i]:
#                 stack.pop()
#             #stack에 남아 있는 큰 수의 index를 저장해놓는다.
#             if len(stack)==0:
#                 ans.append(0)
#                 stack.append(top[i])
#             elif len(stack) !=0:
#                 # print(stack[-1])
#                 # stack.append(top[i])
#                 ans.append(top.index(stack[-1])+1)  #index 찾는 시간 복잡도는 for문과 동일하다 O(N) ....
#                 stack.append(top[i])
#         # print(stack)
#     print(*ans)
#
# if __name__ == '__main__':
#     main()


# aa=[1,2,3,4,5,6]
#
# print(aa.index(1))

############################시간 복잡도 O(N)

import sys
read = sys.stdin.readline
def main():
    N = int(read())
    top = list(map(int, read().split()))
    stack = []
    ans = [0] * N

    for i in range(N):
        # 스택에 아직 처리하지 않은 탑이 있고, 해당 탑이 현재 탑보다 낮을 때 pop
        while stack and top[stack[-1]] <= top[i]:
            stack.pop()

        # 스택이 비어있다면 왼쪽에 9수신할 탑이 없으므로 0을 저장
        if not stack:
            ans[i] = 0
        else:
            # 스택에 남아 있는 탑 중 가장 먼저 수신할 수 있는 탑을 저장
            ans[i] = stack[-1] + 1
        print(ans,stack)
        # 현재 탑을 스택에 추가
        stack.append(i)

    print(*ans)


if __name__ == '__main__':
    main()
