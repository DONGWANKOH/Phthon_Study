import sys
read = sys.stdin.readline


def postOrder(pre_order, in_order):
    size = len(pre_order)   # 전체 트리 사이즈
    if size == 0:   # 사이즈 0이면 탈출
        return
    root = pre_order[0]     # pre_order에서 가장 처음 나온 노드가 현재 트리의 루트임
    left_tree = in_order.find(root)     # in_order에서 root의 인덱스는 왼쪽 서브트리의 자식 개수를 의미
    right_tree = size - left_tree - 1   # 전체 - 왼쪽 서브트리 - 루트 노드. 오른쪽 서브트리의 개수

    postOrder(pre_order[1:left_tree + 1], in_order[0:left_tree])    # 왼쪽 서브트리에 해당하는 부분 잘라서 재귀
    postOrder(pre_order[left_tree + 1:], in_order[left_tree + 1:])  # 오른쪽 서브트리에 해당하는 부분 잘라서 재귀
    print(root, end='')     # post order 이므로 루트가 가장 마지막에 순회됨. 즉 마지막에 처리


def main():
    while True:
        try:
            pre_order, in_order = read().rstrip().split()
            postOrder(pre_order, in_order)
            print()
        except:
            break


if __name__ == '__main__':
    main()