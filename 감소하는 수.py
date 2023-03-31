from itertools import *
#
# for i in range(1,3):
#     a=list(combinations(range(0,i),2))
#     print(a)
# print(len(a)+9)


# for i in range(1,10)
#     for j in range(1,10)
#         combinations(range(0,10),2)
#         b=list(combinations(range(0,10),2))
# print(b)

import sys
from itertools import *
read=sys.stdin.readline
n = int(read())

nums = list()
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        # print(comb)
        comb = list(comb)
        # print(comb)
        # comb.sort()
        # print(comb)
        comb=sorted(comb, key=lambda x:x , reverse=True)
        # print(comb)
        # nums.append(comb)
        # comb=str(comb)
        # nums.append(int(''.join(comb)))
        comb=map(str,comb)
        nums.append(int(''.join(comb)))
# print(nums)
nums.sort()
# print(nums)
# # print(nums[n])

try:
    print(nums[n])
except:                  # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)


# print(len(a)+9)
#
# for i in range(1,)
#     for j in range(0,i)

# for i in range(n):
#     combination(range(1,))
# # for i in range(6,0,-1):
# #     print(i)
# a=[]
# for j in range(0,):
#     # print(type(j))
#     a.append(j)



# for i in range()