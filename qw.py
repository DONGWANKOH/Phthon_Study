import sys
from itertools import *
import copy

read = sys.stdin.readline

a=[1,1,1]*3  정수가 복사됐던 것
print(a)
a[2]=4
print(a)


b=[[0,0,0]]*3 리스트가 복사 됐던 것..

b[0][1]=5
0 5 0
0 5 0
0 5 0 으로 mutable imutable 로 전부다 변경돼 버린다.. Q를 부를 때 deepcopy를 썼다.. call by assignment

for i in range(3):
    for j in range(3):
        print(b[i][j], end=' ')
    print()

###############################
a=[
    [1,1,1]
    [1,1,1]
    [1,1,1]
]
print(a)
b[2][2]=10
print(a)  #b를 바꿨는데 a도 바뀐다.. 이럴 때 deepcopy를 사용한다..


##################################################
b=[]
#temp=[]  #temp에 넣기 때문에 1차원으로 생성 됨.
for i in range(3):
    temp=[]  #temp의 행을 초기화 해서 넣기 위함>>2차원
    for j in range(3):
        temp.append(a[i][j])
    b.append(temp)
b[1][2]=3
print(b)