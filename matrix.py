arr = [['1,2,3', '4,5,6', '7,8,9'], ['a,b,c', 'd,e,f', 'g,h,i']]

result_1 = zip(*reversed(arr))

result_2 = list(zip(reversed(arr)))

result_3 = list(zip(*reversed(arr)))

result_4 = list(map(list, zip(*reversed(arr))))

# print(result_1)
print(result_2)
print(result_3)
print(result_4)
# print(result_1, result_2, result_3, sep = '\n')

# print(result_1, result_2, result_3, sep = '\n')