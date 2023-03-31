import sys

read = sys.stdin.readline

N = int(input())

num = [0 for _ in range(10001)]  # 10001 범위 틀렸었다!!
M = []
Q = 0
ans = 0
어떤게
틀린건지
P = []
O = []
for i in range(N):
    p = int(read().rstrip())
    num[p] = 1
    M.append(p)

Q = max(M)

for i in range(Q + 1):
    ans += num[i]
    P.append(sum(num[i:i + 5]))

for h in P:
    O.append(h - 5)

if max(O) < -5:
    print(0)
elif max(O) == -5:
    print(0)
elif max(O) > -5:
    print(-max(O))