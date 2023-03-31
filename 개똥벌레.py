import sys
read=sys.stdin.readline
N,H=map(int,read().rstrip().split())
a=[]
under=[]
upper=[]
cnt=0
for i in range(N):
    a.append(int(input()))

for i in range(0,N,2):
    under.append(a[i])
for j in range(1,N+1,2):
    upper.append(a[j])

sum=[]

for i in range(0,H+1):
    cnt=0
    for j in range(N//2):
       if under[j]>=i:
           cnt+=1
           # print(cnt)
       if upper[j]>H-i:
           cnt+=1
           # print(cnt)
    # print(cnt)
    # cnt=0
    sum.append(cnt)
# cnt=0
# print(sum)
print(min(sum),sum.count(min(sum)))



