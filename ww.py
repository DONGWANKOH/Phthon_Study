from bisect import bisect_left,bisect_right

import bisect

a=['e','y','q','v','y','e','a','b']
b=[1,3,5,5,7,2]
# b=sorted(b)
# b.sort()
# print(b)

# a=map(ord,a)
# A=bisect(b,5)

A=bisect_left(b,5)
B=bisect_right(a,'e')

print(A)
print(B)