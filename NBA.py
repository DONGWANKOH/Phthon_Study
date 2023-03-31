#최소단위를 기준으로
#1분10초는 70초로 환산 한 다음에 대소관계를 비교 후에
#logic은 마냥 쉽지는 않다.. 이기고 있는 시간을 계산해야한다. 초 단위로 이기고 있는지 확인이 필요하다. 입력 값이 들어간 시점이 변화가 일어난다. 분은 *60초  뒤에는 그냥 더하기(+)

import sys
read=sys.stdin.readline

def main():

    Team=[0 for _ in range(3)]
    time=[0 for _ in range(3)]
    N=int(read().rstrip())
    match=[]
    for i in range(N):
        a,b=read().split()
        # print(a), print(b[0:2]+b[3:5])
        a=int(a)
        h,m=int(b[0:2]),b[3:5]
        match.append((a,int(str(h)+str(m))))
        print(match)
        # print(h,m)
        Team[a]+=1
        time[a]+=int(h)

        if Team[1]>Team[2]:
            time[1] += 48-h-time[2]
        elif Team[1]<Team[2]:
            time[2] += 48-h-time[1]
        else :
            continue
    # print(time[1])
    print(str(time[1]%60)+':'+str(m))
    print('2d : %2d' % (time[2]//60, time[2]%60))

if __name__=='__main__':
    main()