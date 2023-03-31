from bisect import*

def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: (x[1], x[0]))     # 나가는 위치 기준 오름차순 정렬

    cam = -int(1e9)

    for start, end in routes:
        if start <= cam:    # 시작 위치가 카메라 보다 뒤에 있으면 만남
            continue

        cam = end   # 새로운 카멜라 위치는 현재 차가 나가는 위치 지점을 저장
        answer += 1

    return answer

def main():
    routes=[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

    print(solution(routes))

if __name__ == '__main__':
    main()