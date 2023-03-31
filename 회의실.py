#line sweeping문제임

#시작점으로 배열한 경우 case1)
# ------------------------------
  #  ---------- -----------

#계속 손으로 표시하면서 끝나는 시간으로 정렬해야하는지 시작시간으로 정렬해야하는지 표시해야한다..


#import sys
# read=sys.stdin.readline
#
#
# N=int(read())
# meet=[]
# for i in range(N):
#     a,b=map(int,read().split())
#     meet.append((a,b))
#
# meet=sorted(meet, key=lambda x: x[1])
#
# end=-1
# cnt=0
#
# for j in range(len(meet)):
#     start=meet[j][0]
#     if start>2**31-1:
#         break
#     elif start>=end:
#         cnt+=1
#         end=meet[j][1]
#     # print(j,'시간:',start,end, '회의참석 수 :', cnt)
# print(cnt)

############################
import sys
read=sys.stdin.readline

N=int(read())
meet=[]
for i in range(N):
    a,b=map(int,read().split()) #list comprehension이 가독성은 좋지 않다.
    meet.append((a,b))

# 끝나는 시간을 기준으로 정렬하되, 끝나는 시간이 같은 경우 시작시간을 기준으로 정렬
meet=sorted(meet, key=lambda x: (x[1], x[0]))    #2번째 정렬 조건 (1,2) (2,2)  의 경우 (1,2)를 먼저 보지 않으면 값이 1이 된다..
# (2,2)            -
# (1,2)      -------   이런 경우..답이 2인데, 시작시간을 정렬 안 하면 Error
end=-1
cnt=0

for j in range(len(meet)):
    start=meet[j][0]
    end_time=meet[j][1]
    if start>2**31-1 or end_time>2**31-1:
        break
    elif start>=end:
        cnt+=1
        end=end_time

for j in range(len(meet)):
    start=meet[j][0]
    # end_time=meet[j][1]
    if start>2**31-1 or end>2**31-1:
        break
    elif start>=end:
        cnt+=1
        end=meet[j][1]

print(cnt)
