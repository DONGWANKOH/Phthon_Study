import sys
read=sys.stdin.readline


def main():

    N,d,k,c=map(int,read().split())

    susi=[]
    for i in range(N):
        num=int(read())
        susi.append(num)

    susi=susi+susi[:k-1]  #회전초밥에서 가능한 연속된 초밥 번호
    wagu=0
    for j in range(N):
        eat=susi[j:j+k]
        dish=set()
        for i in eat:
            dish.add(i)
        dish.add(c)
        # print(dish)
        wagu=max(len(dish),wagu)

    print(wagu)

if __name__=='__main__':
    main()