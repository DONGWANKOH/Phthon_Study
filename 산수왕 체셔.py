import sys

# sys.setrecursion(10**9)
read=sys.stdin.readline


A,B,C=map(int,read().split())

def cal(A,B,C):
    if B==1:
        return A%C
    # else :
    #     ans=cal(A,B//2,C)
    #     if B%2==0:
    #         return ans*ans%C
    #     else :
    #         return ans*ans *A % C
    else:

        if B % 2 == 0:
            return cal(A,B//2,C) * cal(A,B//2,C) % C
        else:
            return cal(A,B//2,C) * cal(A,B//2,C)*A % C
        # res=A**B%C
        # return cal(A,B//2,C)

print(cal(A,B,C))



# [문제]
# N개의 수가 주어지고, 이 중에서 연속된 수들을 선택하여 구할 수 있는 합 중에서 가장 큰 합을 구하는 문제입니다.
# 단, 선택된 수들은 서로 인접하면 안 됩니다.
#
# [입력]
# 첫 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄에는 N개의 정수가 주어집니다.
# 각 정수는 절댓값이 1,000을 넘지 않습니다.
#
# [출력]
# 첫째 줄에 구한 합을 출력합니다.
#
# [예제 입력]
# 10
# 10 -4 3 1 5 6 -35 12 21 -1
#
# [예제 출력]
# 33

n = int(input())
nums = list(map(int, input().split()))

# 첫 번째 수부터 차례대로 더해나가는데,
# 더한 결과가 0 미만이면 다음 숫자부터 다시 더해나갑니다.
# 최대값은 max_sum에 저장됩니다.

# cur_sum = max_sum = nums[0]
# for num in nums[1:]:
#     cur_sum = max(num, cur_sum + num)
#     max_sum = max(max_sum, cur_sum)
# print(max_sum)



for i in range(n):
    num
    nums[i]=max(nums[i], nums[i]+nums[i-1])

print(nums)
print(max(nums))