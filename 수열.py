# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
import sys
read = sys.stdin.readline
#누적합, 투포인터, 슬라이딩 윈도우에 대하여 공부가 필요하다.
#psum에 대한 부분 확인 구간의 합을 구할 수 있다 1번부터 쓰는 습관을 들여라. 처음에는 0이 넣어지게..

#이중 for문은 절대 안 된다. 2이상 100,000이기 때문에 안 된다.
# 슬라이싱 자체가 for문 하나라고 본다.  i~얼마까지 도는 거다..sum의 연산이 for문 하나라고 생각하면 될듯????

N,M=map(int,read().split())
temp=list(map(int,read().split()))
ans=[]
res=sum(temp[0:M])
ans.append(res)

#투포인터로 이동하면서 max값으로 업데이트 하는 윈도우 슬라이싱을 하자
#계속 sum을 하면 시간복잡도가 어떻게 되는지 고민해보자...


for i in range(len(temp)-M):
   res-=temp[i]
   res+=temp[i+M]
   ans.append(res)

print(max(ans))

#############시간 초과####### 완전 탐색
'''
for i in range(len(temp)-M):
   p.append(sum(temp[i:i+M]))
# print(p)
print(max(p))
'''

#정답 : 누적합
# import sys
# read = sys.stdin.readline
#
# INF = 1e9
#
# def main():
#     N, K = map(int, read().rstrip().split())
#     a = list(map(int, read().rstrip().split()))
#     # 누적합 저장할 배열
#     psum = [0]  # 인덱스를 1부터 시작해야 psum[i]가 i까지의 누적합이 됨
#
#     for i in range(len(a)):
#         psum.append(psum[i] + a[i]) # psum은 인덱스가 1부터 시작하고 a는 0부터 시작함
#
#     res = -INF  # 최댓값을 구해야 하므로 터무니 없이 작은 수로 초기화
#
#     for i in range(K, N + 1):
#         res = max(res, psum[i] - psum[i - K])   # 연속 K일의 합 최댓값 갱신
#
#     print(res)
#
#
# if __name__ == '__main__':
#     main()


##정답 슬라이싱 윈도우

# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# global a, res, N, K
#
#
# def main():
#     global a, res, N, K
#     N, K = map(int, read().rstrip().split())
#     a = list(map(int, read().rstrip().split()))
#     psum = sum(a[0:K])     # 0번부터 K개의 원소 합 미리 구하기
#     res = psum    # 처음 K개 값을 저장해놓고 이 후에는 최댓값 갱신하면서 답 찾아야 됨
#
#     for i in range(K, len(a)):
#         psum += a[i] - a[i - K]  # 2개 전의 값은 빼주고 현재 값을 더해서 영역을 슬라이딩 하듯이 밀면서 확인
#         res = max(res, psum)
#
#     print(res)
#
#
# if __name__ == '__main__':
#     main()