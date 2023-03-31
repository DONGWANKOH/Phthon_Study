import sys
n  = int(input())
A = list(map(int,sys.stdin.readline().split()))
stack = [0]
# -1 로 초기화
ans = [-1 for i in range(len(A))]


for i in range(1,len(A)):
    #스택에 대한 조건을 먼저 넣는것이 중요함.
    #스택이 차있고, 비교하려는 값이 스택의 맨위인덱스(의 값)보다 크다면
    while stack and A[i] > A[stack[-1]] :
        ans[stack.pop()] =  A[i]
    #바로위에  Pop 못했더라도 스택에 쌓기
    stack.append(i)
print(*ans)