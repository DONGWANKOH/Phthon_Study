
import sys

read = sys.stdin.readline

def main():
    V, E = map(int, read().rstrip().split())
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    # 출력 조건 맞게 설정
    # [먼저][나중] = -1, [나중][먼저] = 1
    for _ in range(E):
        start, end = map(int, read().rstrip().split())
        graph[start][end] = -1
        graph[end][start] = 1

    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                # 1 -> 2 이고 2 -> 3 이면 1 -> 3을 확인할 수 있음. [i][k] == [k][j]]인 경우
                # 1 -> 2 이고 3 -> 2 이면 1 -> 3을 확인할 수 없음 [i[k] != [k][j]인 경우
                if graph[i][k] != 0 and graph[i][k] == graph[k][j]:
                    graph[i][j] = graph[i][k]

    s = int(read().rstrip())
    b=[]
    for _ in range(s):
        start, end = map(int, read().rstrip().split())
        b.append(graph[start][end])

    for t in range(len(b)):
        print(b[t])

if __name__ == '__main__':
    main()
