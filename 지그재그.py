# [문제]
# 자연수 N이 주어졌을 때, 1부터 N까지의 자연수를 지그재그 형태로 출력하는 프로그램을 작성하시오. 지그재그 형태란 첫 번째 줄은 왼쪽에서 오른쪽으로, 두 번째 줄은 오른쪽에서 왼쪽으로, 세 번째 줄은 왼쪽에서 오른쪽으로, 이와 같이 바뀌면서 출력하는 형태를 말한다.
#
# [입력]
# 자연수 N이 입력으로 주어진다. (1 ≤ N ≤ 100)
#
# [출력]
# 지그재그 형태로 1부터 N까지의 자연수를 출력한다. 각 줄에는 10개까지 출력하며, 한 줄에 출력된 숫자는 공백으로 구분한다.
#
# [예제 입력]
# 10
#
# [예제 출력]
# 1 2 3 4 5 6 7 8 9 10
# 20 19 18 17 16 15 14 13 12 11
# 21 22 23 24 25 26 27 28 29 30
# 40 39 38 37 36 35 34 33 32 31
# 41 42 43 44 45 46 47 48 49 50
# 60 59 58 57 56 55 54 53 52 51
# 61 62 63 64 65 66 67 68 69 70
# 80 79 78 77 76 75 74 73 72 71
# 81 82 83 84 85 86 87 88 89 90
# 100 99 98 97 96 95 94 93 92 91
#
# [힌트]
# 예제 출력에서와 같이 1부터 10까지 출력하는 경우 첫 번째 줄은 1부터 10까지 출력하고, 두 번째 줄은 20부터 11까지 출력한다.
# 그리고 세 번째 줄은 다시 21부터 30까지 출력하고, 네 번째 줄은 40부터 31까지 출력한다. 이와 같이 지그재그로 출력한다.

n = int(input())

# 각 줄에서 출력할 시작번호와 끝번호를 계산하는 함수



# def calc_range(line):
#     if line % 2 == 1:  # 홀수 줄
#         start = (line-1)*10+1  #10x+1 /  x= 1,2,3,4,5,6...
#         end = start + 9
#     else:  # 짝수 줄
#         end = line*10 #10x /  x= 1,2,3,4,5,6...
#         start = end - 9
#     return (start, end)
#
# for i in range(1, n+1):
#     start, end = calc_range(i)
#     # 각 줄에서 출력할 숫자들을 리스트로 만듦
#
#     nums = list(range(start, end+1))
#     print(nums)
#     if i % 2 == 0:  # 짝수 줄인 경우 뒤집어서 출력
#         nums = nums[::-1]
#     # 리스트를 공백으로 구분하여 출력
#     print(' '.join(map(str, nums)))


###################################################
def calc_range(line):
    start = (line-1)*10+1  #10x+1 /  x= 1,2,3,4,5,6...
    end = start + 9
    return (start, end)

for i in range(1, n+1):
    start, end = calc_range(i)  #함수를 통해서 변수 2개를 지정 받을 수 있다.

    # 각 줄에서 출력할 숫자들을 리스트로 만듦

    nums = list(range(start, end+1))  #range의 수를 list로 할 수 있는 구현 능력
    # print(nums)
    if i % 2 == 0:  # 짝수 줄인 경우 뒤집어서 출력
        nums = nums[::-1]  #뒤집어서 출력하는 코딩...
    # 리스트를 공백으로 구분하여 출력
    print(' '.join(map(str, nums)))  #join은 str type에서만 된다!!!!!!!!!!!!!!

##################

# 위 코드에서 calc_range 함수는 지그재그로 출력할 각 줄에서 출력할 시작번호와 끝번호를 계산합니다.
# 이 함수는 현재 줄이 홀수인지 짝수인지를 판단하여, 홀수인 경우 (현재 줄 번호 - 1) x 10 + 1부터 시작하고 9를 더한 값까지 출력하고,
# 짝수인 경우 현재 줄 번호 x 10부터 시작하고 9를 빼서 끝번호를 계산합니다.
#
# 메인 코드에서는 calc_range 함수를 이용하여 각 줄에서 출력할 숫자들을 리스트로 만들어서, 짝수 줄일 경우 숫자들을
# 뒤집어서 출력합니다. 그리고 리스트를 join 함수를 이용하여 공백으로 구분하여 출력합니다.