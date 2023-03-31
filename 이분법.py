import sys
read=sys.stdin.readline
day=[]
money=[]
N,M=map(int(read().split())

for i in range(N):
    day.append(int(input()))

for i in range(1,10001):
    money.append(i)

lo=0
hi=len(money)
need_money=(hi+lo)//2

def cal_money(N,M):

    # for i in range(0,N):
    #     B.sum(day[0:i])
    for i in day:
        Change=need_money-i
        if Change>=0:
            n+=1
            if n==M:
                return
            continue
        else:
            Change+need_money-B

print(day)


# def cal_money(N,M):
#
#     if sum(day)%M>0:
#         need_money=sum(day)//M+2
#
#     for i in range(N,0,-1):
#         if sum(day[0:i])>need_money
#             cal_money(N-1)
#
#         while lo <= hi:  #data가 하나만 남았을 때
#             mid=(lo+hi)//2
#             M=sum(day) // money[mid] > 0:
#             if M>0:
#                 if sum(day)//K==M:
#                     return need_money
#                 elif data[mid] < m:
#                     lo=mid+1
#                 else :
#                     hi=mid-1
#
#         return  'No'
#
# print(day)
