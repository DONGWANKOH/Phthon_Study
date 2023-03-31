import sys
read=sys.stdin.readline

def main():
    N=int(input())
    a=[[0 for _ in range(N)]]
    b=[0 for _ in range(N)]
    c=[[0 for _ in range(N)] for _ in range(N)]
    d=[]
    e=[]
    for i in range(N):
        d.append(list(map(int,read().rstrip())))



    for i in range(N):
        data = [int(x) for x in input().split()]
        e.append((data[0], data[1], data[2]))



    for i in range(N):
        for j in range(N):
          print(c[i][j],end=' ')
        print()

    print(a)
    print(b)
    print(c)
    print(d)
    print(data)
    print(e)


if __name__=='__main__':
    main()
