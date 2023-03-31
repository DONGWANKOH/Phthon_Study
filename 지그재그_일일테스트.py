# 입력받은 n, r, c 값을 각각 n, r, c 변수에 저장합니다.
n, r, c = map(int, input().split())

# 현재 영역의 크기 margin, x좌표 x, y좌표 y를 입력받아서 처리하는 재귀 함수입니다.
def recurse(margin, x, y):
    # margin이 1이라면 현재 영역이 1x1 크기의 정사각형이므로 해당 영역에 대한 정보를 반환합니다.
    # 이 값은 0으로 설정해줍니다.
    if margin == 1:
        return 0

    # 현재 영역을 4개의 사분면으로 나누어 재귀적으로 recurse() 함수를 호출합니다.
    # 이때 margin 값을 절반으로 나누어 각 사분면의 크기를 결정하고,
    # (x, y) 좌표가 어느 사분면에 속하는지를 판단하여 해당 사분면으로 이동합니다.
    margin //= 2
    for i in range(2):
        for j in range(2):
            if x < margin * (i + 1) and y < margin * (j + 1):
                # 현재 좌표 (x, y)가 어느 사분면에 속하는지 계산합니다.
                # 좌표 (x, y)가 속한 사분면 내에서의 위치는 (x - margin * i, y - margin * j)입니다.
                # 이 위치를 바탕으로 재귀적으로 recurse() 함수를 호출하여 반환된 값을 이용해
                # 현재 사분면 내에서 (x, y) 좌표가 어느 위치에 속하는지를 계산합니다.
                return (i * 2 + j) * margin**2 + recurse(
                    margin, x - margin * i, y - margin * j
                )

# recurse() 함수를 호출하여 출력합니다.
print(recurse(2**n, r, c))
