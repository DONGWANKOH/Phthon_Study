import sys
read = sys.stdin.readline


def calc(numbers):
    sum = 0
    # 숫자 두 개씩 묶어서 곱해서 더하기
    for i in range(0, len(numbers), 2):
        sum += numbers[i] * numbers[i + 1]
    return sum


def main():
    N = int(read().rstrip())
    positive = []   # 양수 담을 배열
    negative = []   # 음수 담을 배열
    zero = False
    res = 0

    for _ in range(N):
        x = int(read().rstrip())

        # 0은 따로 표시. 음수가 짝수개 있으면 마지막 숫자에 곱하는 용도로 사용할 것임.
        # 음수가 짝수개면 둘이 곱하면 되는거 아닌가?? 뒷부분 Logic에 무조건 곱하기 때문에 끝에 1을 추가함> 때문에 짝수개면>>홀수개이다.
        # 그 외의 경우에는 +0으로 처리하여 무효화 하는 것이 가장 큰 결과를 얻음
        if x == 0:
            zero = True
        # 1은 다른 수에 곱하는 것 보다 +1을 하여 결과값에 1을 더하는 것이 최적
        elif x == 1:
            res += 1
        # 음수인 경우 따로 저장
        elif x < 0:
            negative.append(x)
        # 양수인 경우 따로 저장
        else:
            positive.append(x)

    positive = sorted(positive, reverse=True)
    negative.sort()

    # 홀수개 이면 뒤에 1을 넣어서 두개씩 묶기 편하게 만들기
    if len(positive) % 2 == 1:
        positive.append(1)

    # 홀수개 인 경우 만약 입력에 0이 있었다면 하나 남은 음수를 없앨 수 있으므로 제거해 버리기
    # 0이 없었다면 1을 넣어 두개씩 묶기 편하게 만들기
    if len(negative) % 2 == 1:
        if zero:
            negative.pop()
        else:
            negative.append(1)

    res += calc(positive)
    res += calc(negative)

    print(res)


if __name__ == '__main__':
    main()