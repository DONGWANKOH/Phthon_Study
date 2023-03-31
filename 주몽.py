# 6
# 9
# 2 7 4 1 5 3

#2개를 조합해야하는 경우는 투포인터 확률이 높다.
#이분탐색은 만 단위가 아니고 엄청 크다 1000만 단위
#시간복잡도 NlogN


import sys
read=sys.stdin.readline

N=int(read().rstrip())
M=int(read().rstrip())
material=list(map(int, read().split()))

material.sort() #정렬이 NlogN이다. 최대시간이 정렬이 걸린다.
# print(material)
l=0
r=N-1
cnt=0

# def search(l,r):
# global cnt
while l<r:
    if material[l]+material[r]==M: # 투 포인터의 경우 5 / 2 / 1 1 1 1 1 입력 시 경우의 수 10이 나와야한다.
        cnt+=1
        l+=1
        # r-=1
    elif material[l]+material[r]<M:
        l+=1
    elif material[l] + material[r] > M:
        r-=1
        # if l>=r:
        #     break


# for i in range(r):
#     search(i,r)

print(cnt)



##########조합 시간 초과#############
# import sys
# from itertools import*
#
# read=sys.stdin.readline
# N=int(read().rstrip())
# M=int(read().rstrip())
# material=list(map(int, read().split()))
# ans=[]
#
# for i in combinations(material,2):
#     if sum(i)==M:
#         ans.append(i)
# print(len(ans))