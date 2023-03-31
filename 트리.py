# 5
# -1 0 0 1 1
# 2
#tree = [-1,0,0,1,1], [-1,0,-10,1,1]


import sys
read=sys.stdin.readline

def dfs(d):
    global tree,m,N

    tree[d] = -10 #tree에 삭제할 노드 값을 변경한다.
    print(tree)
    for i in range(N): #반복문을 통해 제거할 노드의 리프노드들을 확인하고 재귀를 타서 진행한다/ >>  값들을 모두 찾아내기//
        if d==tree[i]: #부모 노드를 저장하고 있는 tree에서 삭제할 -10이 있는 경우 dfs를 지속 진행하여 리프노드들을 찾아낸다.
            dfs(i)

def main():
    global m,tree,N

    N=int(read())
    tree = list(map(int,read().split()))
    # tree=list(enumerate(map(int,read().split()),start=1))
    m=int(read())
    cnt=0

    dfs(m)

    for i in range(N):
        if tree[i] !=-10 and i not in tree:
            # 삭제할 노드 값을 -1보다 작은 수로 변경 >> 입력하고 변경값 -10이 아니고  #리프노드인 경우,,tree에 없는 경우 cnt+=1을 한다.
            cnt+=1
    print(cnt)

if __name__ == '__main__':
    main()