# 3 4
# c..c
# ..c.
# ....
import sys
from bisect import bisect_left, bisect_right
read=sys.stdin.readline
#
# nums = [0,1,2,3,4,5,6,7,8,9]
# n = 5   0 1 2 3 4 >
#
# print(bisect_left(nums, n))  >>5
# print(bisect_right(nums, n)) >> 6



# A=[1,2,3,4]
# print(A.index(1))

N,M=map(int,read().split())
matrix=[]
ans=[[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    matrix.append(read().rstrip())

# print(matrix[2][:8])


for o in range(N):
    for p in range(M):
        if matrix[o][p]=='c':
            ans[o][p]=0
        elif matrix[o][p]=='.':
            if 'c' in matrix[o] :
                # print('들어가지는지 확인')
                # print('확인하는 부분',matrix[o][:p])
                # print('p',p,bisect_right(matrix[o],'c'))
                ans[o][p]=p-bisect_right(matrix[o][:p],'c')+1 #ans[o][p]=p-bisect_right(matrix[o][:p],'c')+1

            else :
                ans[o][p] = -1
        # print(ans[o][p],end=' ')
    print()


# print(ans)
###################################정답 코드###########

import sys
read = sys.stdin.readline


def main():
    H, W = map(int, read().rstrip().split())
    a = []
    for _ in range(H):
        c = list(map(str, read().rstrip()))     # 문자열일때도 map 사용 가능
        c.append(0)     # 구름 확인할 때 map 벗어나는거 체크 안하기 위해, 메모리를 좀더 사용하지만 끝부분 처리를 위하여 사용함
        a.append(c)

    # 구름이 안 왔다는 전제로 -1로 초기화
    res = [[-1 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if a[i][j] != 'c':  # 구름이 아닌 경우 무시  ##j가 올라간다...
                continue

            res[i][j] = 0   # 현 위치에 구름이 있으므로 0으로 변경
            cnt = 1     # 동쪽으로 몇번만에 가는치 확인할 변수
            while a[i][j + 1] == '.':   # 다음 위치에 구름 없는 경우. 위에서 0넣은건 while문 안으로 안들어와서 확인 안해봐도 됨
                res[i][j + 1] = cnt
                cnt += 1    # 다음번 위치에 구름 없을 경우 사용하기 위해
                j += 1      # 구름 동쪽으로 이동

    for i in range(H):
        for j in range(W):
            print(res[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()