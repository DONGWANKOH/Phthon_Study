from math import sqrt
import sys
from itertools import *
read=sys.stdin.readline
#
from math import sqrt

# while True:
#     if sum>N:
#         sum-=num[lo]
#         lo+=1
#     elif len(num)==hi:
#         break
#     elif sum<=N:
#         sum+=num[hi]
#         hi+=1
#
#     if sum==N:
#         res+=1

P=['1','2','3']
W=[1,2,3]
Q=''.join(map(str,W))
print(Q)


##1.소수 뽑기
# composite=[False for _ in range(2,N+1)]
# N=int(read())
#
# for i in range(2,int(sqrt(N)+1)):
#     if composite[i]:
#         continue
#     for j in range(i*2,N+1,i):
#         composite[i]=True


##2.itertools 활용

# for c,s in zip(count(0,0.5),'abc'):
#     print(c,s)
# print('--------------------------')
# for c,s in zip(range(2),'abcdefghig'):
#     print(c,s)
# print('--------------------------')
# num=[]
# for c, s in zip(range(2), 'abcdefghig'):
#     print(c, s)
#     num.append([c,s])
# print(num)
# print('--------------------------')

# print(pow(2,3))

# for c,s in zip(cycle(range(2)),'abcdefghig'):
#     print(c,s)
# print('--------------------------')
# for c,s in zip(cycle('13'),'abcdefghig'):
#     print(c,s)