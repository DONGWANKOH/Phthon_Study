import sys
read=sys.stdin.readline

N=int(read())
team=[]
Alpa_list=[0 for _ in range(26)]
i2c='abcdefghijklmnopqrstuvwxyz'

ord(a) =64

char(64) = a
ans=[]
for i in range(N):
    car=read().rstrip()
   team.append(car)

for i in team:
    Alpa_list[(ord(i[0])-ord('a'))]+=1

for j in range(len(Alpa_list)):  #index상 한 번 더 고민했다.
    if Alpa_list[j]>=5:
        ans.append(i2c[j])
    # elif Apla_list

# print(team)
# print(Alpa_list)
'''
if all(Alpa_list)<=5:
    print('PREDAJA')
else:
    for i in range(len(ans)):
        print(ans[i], end='')
'''
if len(ans)==0:  #이 부분을 고민했다
    print('PREDAJA')
else:
    for i in range(len(ans)):
        print(ans[i], end='')

'''  
if any(Alpa_list)>0:
    for i in range(len(ans)):
        print(ans[i], end='')
else :
    print('PREDAJA')
    '''
####################미진#########
# import sys
# read = sys.stdin.readline
#
#
# n = int(read())
#
# dic ={}
#
# for i in range(n):
#     temp = read().rstrip()
#     if temp[0] in dic:
#         dic[temp[0]] += 1
#     else:
#         dic[temp[0]] = 1
# li = []
# for i, v in dic.items():
#     if v >= 5:
#         li.append(i)
# li.sort()
# if len(li) == 0:
#     print('PREDAJA')
#
# else:
#     # for i in li:
#     #     print(i, end = '')
#     print(''.join(li))


############정답
#장바구니에 상품을 담는 경우 많이 쓰인다..######
import sys
read = sys.stdin.readline


def main():
    # 알파뱃을 셀 배열. 알파뱃이 26개 이므로.
    counting = [0 for _ in range(26)]

    N = int(read().rstrip())

    # 5번 나왔으면 True로 바꿈
    flag = False

    for i in range(N):
        s = read().rstrip()
        # 첫 글자만 카운팅
        counting[ord(s[0]) - ord('a')] += 1

    for i in range(26):
        if counting[i] >= 5:
            flag = True
            # 아스키 코드를 문자로 바꿔서 출력
            print(chr(i + ord('a')), end='')

    # True로 바뀌지 않았으면 5 이상인 경우가 없었다는 의미
    if not flag:
        print("PREDAJA")


if __name__ == '__main__':
    main()