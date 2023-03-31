# DBACEGF ABCDEFG
# BCAD CBAD

import sys
from bisect import *

read = sys.stdin.readline


def devide(pre, ino):
    # return left,right


    n = bisect_left(ino, pre[0])
    ino = [ino[:n],ino[n + 1:]]
    # print(pre[0], end=' ')
    pre = pre[1:]

    for i in ino:
        devide(pre, i)

    for j in range(len(pre),-1,-1):
        print(pre[i])

    if len(pre) == 1:
        for i in range(len(ino), -1, -1):
            print(pre[i], end=' ')

        return left, right
    devide(pre, right)


def main():
    while True:
        try:
            pre_order, in_order = read().rstrip().split()
            print(devide(pre_order, in_order))

        except:
            break


if __name__ == '__main__':
    main()