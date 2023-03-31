#1번 풍선을 한 번 맞춥니다.
# 2번. 오른쪽으로 시선을이동하며 아직 터지지 않은 풍선 M개를 지나칩니다.
# 3번. 현재 보고 있는 풍선을 한 번 맞춥니다.
# 4번.아직 터지지 않은 풍선이 남아있다면 2,3번 과정을 반복합니다
#
# 풍선을 터트릴 때, 풍선을 터트린 순서를 구하는 프로그램을 작성하세요.

#풍선은 회전판 형식, 1번부터 N번까지 N개의 풍선, m은 M번씩 이동할 입력값

from collections import deque

_, m = map(int, input().split())
d = deque([i, baloon] for i, baloon in enumerate(map(int, input().split()), 1))
res = []
print(d)
while d:
    # print(d[0][0])
    d[0][1] -= 1

    if d[0][1] == 0:
        res.append(d.popleft()[0])
    else:
        d.rotate(-1)
    d.rotate(-m)
print(*res)