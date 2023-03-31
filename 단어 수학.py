import sys
read=sys.stdin.readline

# num=[9,8,7,6,5,4,3,2,1]
N=int(read().rstrip())
word_list=[[0 for _ in range(8)] for _ in range(N)] #숫자의 최대 길이는 8
word=[]
word_num=0


for i in range(N):
    word.append(list(read().strip()))


for p in word:
    end = 8 - len(p)
    for q in p:
        word_list[word_num][end]=q
        end+=1
    word_num+=1
print(word_list)

for i in zip(*word_list):
    print(i)

w=0
num=9
m_list=[]

for i in range(8):
    for j in range(N):
        if type(word_list[j][i])==str and word_list[j][i] in m_list :
            word_list[j][i]=num
            m_list.append(word_list[j][i])
            num-=1

# for i in zip(*word_list):
#     for j in i:
#         print(j)
#         if type(j)==str:
#             j=num
#             num-=1
print(word_list)
sum=0

for i in word_list:
    y = 7
    for j in i:
        sum+=j*(10**y)
        y-=1
print(sum)

# print(word_ans)
# print(''.join(word_list[k]))
# ans=''.join
#
# for i in zip(*word_list):
#     print(i)
#     # for j in i:
#     #     print(j)





