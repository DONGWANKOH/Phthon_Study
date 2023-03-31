#전역변수 a를 practice 함수에서 변경하여 for문을 break하면 나가져서 a는 변경값으로 출력된다!!!!!!!!!!!
for i in [(r, c), (r, c + (size // 2)), (r + (size // 2), c), (r + (size // 2), c + (size // 2))]:
    nr, nc = i 
                    paper(nr, nc, size // 2)
a=0

def practice(n):
    global a
    for i in range(n):
        if a>5:
            return #break
    a+=2
    # practice(a)

def main():
    n=int(input())
    practice(n)
    print(a)
if __name__=='__main__':
    main()