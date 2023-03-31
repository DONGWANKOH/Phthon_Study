n=5
m=3

sum_list=[0 for _ in range(1,m+1)]

if m==0:
    print(sum_list)

# for i in range(1,n-i):
#     for j in range(1,m+1):
#         sum_list[i]=j
#         sum_list.append(sum_list[i])
#     print(sum_list)
# print(sum_list[1:])

for i in range(1,m+1):
    for j in range(n-i,n):
        sum_list[i]=j
        # sum_list.append(sum_list[i])
    print(sum_list)
print(sum_list[1:])