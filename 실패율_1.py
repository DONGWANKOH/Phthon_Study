#시간 복잡도 O(NlogN)
#분모에 0이 위치하여 Error나는 경우, Built in code 가 빠르다...
import sys
read=sys.stdin.readline


def solution(n, stages):
    num_players = len(stages)
    num_stages = [0] * (n+2) # 0~n+1 스테이지 까지 저장할 공간

    # 각 스테이지에 머물러 있는 플레이어 수를 계산
    for stage in stages:
        num_stages[stage] += 1

    # 실패율 계산
    failure_rate = []
    for i in range(1, n+1):
        if num_players == 0:
            failure_rate.append((i, 0))
        else:
            rate = num_stages[i] / num_players
            failure_rate.append((i, rate))
            num_players -= num_stages[i]

    # 실패율을 기준으로 정렬
    failure_rate.sort(key=lambda x: (-x[1], x[0]))

    # 정렬된 스테이지 번호를 반환
    answer = [stage[0] for stage in failure_rate]
    return answer

def main():
    N=int(read())
    stage=list(map(int,read().split()))
    print(solution(N,stage))

if __name__=='__main__':
    main()