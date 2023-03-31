import sys
read=sys.stdin.readline


def main():

    N,d,k,c=map(int,read().split())

    susi=[]
    for i in range(N):
        num=int(read())
        susi.append(num)

    susi=susi+susi[:k-1]  #회전초밥에서 가능한 연속된 초밥 번호
    zero=987654321
    for j in range(N):  #이중 for문 제거.......
        eat=susi[j:j+k]
        dish = [0] * (d + 1)
        for j in eat:
            dish[j]+=1
        dish[c]+=1

        x=dish.count(0)
        zero=min(x,zero)

    print(d-zero+1)

if __name__=='__main__':
    main()