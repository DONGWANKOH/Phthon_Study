# [문제]
# 주어진 행렬 A와 정수 n에 대하여, A^n을 계산하는 문제입니다. 단, n은 양의 정수입니다.
#
# [입력]
# 첫 번째 줄에는 행렬 A의 크기인 정수 m과 n이 주어지며(1 ≤ m ≤ 5), 두 번째 줄부터 m개의 줄에 걸쳐 행렬 A의 원소들이 주어집니다. 그 다음 줄에는 n이 주어집니다(1 ≤ n ≤ 100,000,000).
#
# [출력]
# 행렬 A^n을 출력합니다. 모든 원소는 1,000을 넘지 않는 정수입니다.
#
# [예제 입력]
# 2 2
# 1 1
# 1 0
# 3
#
# [예제 출력]
# 2 1
# 1 1
#
# [힌트]
# A = [[1, 1], [1, 0]], n = 3인 경우, A^3 = [[3, 2], [2, 1]]입니다.
# 행렬 거듭제곱을 계산하는 방법 중 하나는 분할 정복(divide and conquer)을 이용하는 것입니다. 다음은 파이썬으로 구현한 행렬 거듭제곱 코드입니다.


# 위 코드에서 matrix_multiply 함수는 두 행렬의 곱을 계산하는 함수입니다. matrix_power
# 함수는 분할 정복을 이용해 행렬 거듭제곱을 계산하는 함수입니다. 기저 사례인 n = 1인 경우는 행렬 그대로를 반환하고,
# 그 외의 경우에는 n을 반으로 나눈 후 재귀적으로 행렬 거듭제곱을 계산합니다. 행렬 거듭제곱에서는 거듭제곱 수가 짝수인
# 경우에는 중간 과정을 이용해서 더 빠르게 계산할 수 있습니다.
#
# 마지막으로, 입력을 받아서 matrix_power 함수를 호출하고, 그 결과를 출력합니다. 출력할 때는 각 행의 원소를 공백으로
# 구분하여 출력합니다.


# 행렬 곱셈 함수
def matrix_multiply(matrix1, matrix2):
    # 두 행렬의 곱을 구합니다.
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                result[i][j] %= 1000
    return result


# 행렬 거듭제곱 함수
def matrix_power(matrix, n):
    # 기저 사례: n = 1인 경우
    if n == 1:
        return matrix

    # 분할 정복을 이용해 행렬 거듭제곱을 계산합니다.
    temp = matrix_power(matrix, n // 2)
    if n % 2 == 0:
        return matrix_multiply(temp, temp)
    else:
        return matrix_multiply(matrix_multiply(temp, temp), matrix)


# 입력을 받습니다.
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

# 행렬 거듭제곱을 계산합니다.
result = matrix_power(matrix, n)

# 결과를 출력합니다.
for row in result:
    print(*row)
