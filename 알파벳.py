#계수 정렬을 사용하기 좋다.
#계수 정렬, O(N+K)
# 3,1,4,4,2,5,9,10,1,2,1,8,7 - 12개
# 배열을 하나 작성 0~10까지 index
# 숫자가 몇 번 나왔는지
# print(counting한다)
# 숫자     : 0 1 2 3 4 5 6 7 8 9 10  -->숫자 범위가 촘촘하고 반복이 많이 일어날 때 유리하다..
# 나온 횟수 : 0 3 2 1 2 1 0 1 1 1 1
#
# 1을 3번 출력, 2를 2번, 3을 1번 출력..

import sys
read=sys.stdin.readline

car=read().rstrip()
res=set()
ans=[0 for _ in range(26)]

# for i in car:
#     res.add(i)
# res.sort()
# print(sorted(res))  #sorted는 먹히고 sort는 안 먹힌다.

for i in car:
    ans[ord(i)-ord('a')]+=1  #i는 for문에서 받는 거로


    # print(ans[ord(i)-ord('a')])
# print(ord('a')-ord('a'))
print(*ans)

##########################################################
####미진###
# import sys
#
# read = sys.stdin.readline
#
# sen = read().rstrip()
#
# alpha = 'abcdefghijklmnopqrstuvwxyz'
#
# dic = {}
# for i in alpha:
#     dic[i] = 0
# for i in sen:
#     dic[i] += 1
# for k, v in dic.items():
#     print(v, end=" ")
