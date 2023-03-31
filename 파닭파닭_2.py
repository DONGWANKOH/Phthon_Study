#input값을 보고 알고리즘을 선택해야 한다.
#이분 탐색 법으로 풀어야한다. 나무 자르기 #10,000부터는 이중for문 안 된다..

#1번 코드
import sys

read = sys.stdin.readline

def check(mid):
    global N, M, pa, res,cnt
    sum = 0

    for i in pa:
        # 절단기 높이가 더 높으면 파가 안잘림. 음수값이 나와 잘못된 결과 도출
        # if mid >= i:
        #     cnt+=1
        #     continue
        sum += i // mid

    # 자른 길이는 M은 되어야 함
    return sum >= M

def main():
    global N, M, pa
    N,M=map(int,read().split())
    pa=[]
    for i in range(N):
        pa.append(int(read().rstrip()))
    # pa=sorted(pa, reverse=True)

    lo = 1 #min(pa)
    hi = max(pa)
    res=0 ######### 선언

    while lo <= hi:  #등호가 안 들어가면

        mid = ( lo+ hi) // 2
        # 길이가 M 만큼 확보 된 경우. 우리는 이 중에 최소값을 원함. 최소가 되려면 절단기 높이가 최대가 되어야 함
        if check(mid):
            lo = mid + 1
            res = mid
        else:  # 길이가 M 만큼 확보 안된 경우. 더 많이 자르려면 높이를 낮춰야 됨.

            hi = mid - 1

    # print(res)
    print(sum(pa)-res*M)

if __name__ == '__main__':
    main()