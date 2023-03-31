# 4
# 120 110 140 150
# 485

import sys
read=sys.stdin.readline

N=int(read())
a=list(map(int,read().rstrip().split()))

lo=0
hi=max(a)

bugget=int(read())


while lo<=hi:
    mid=(lo+hi)//2
    sum = 0
    for i in a:

        if i>mid:  ### sum+=min(i,mid)
            sum+=mid
        else:
            sum+=i
    if sum>bugget:
        hi=mid-1
    else:           #합이 예산과 같아지는 경우가 포함돼 있어야 한다.
        lo=mid+1
    print(hi,lo, mid,sum)
# print(mid,sum)
print(hi)