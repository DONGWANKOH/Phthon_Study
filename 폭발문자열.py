import sys
from bisect import *
read=sys.stdin.readline

def check(word,boom):
    stack_1 = []
    stack_2 = []
    cnt=0
    for i in word:
        stack_1.append(i)
        if cnt==len(boom):
            break
        elif stack_1[-1] == boom[0]:
            for j in boom:
                stack_2.append(j)



def main():

    word=list(map(ord,read().rstrip()))
    boom=list(map(ord,read().rstrip()))






if __name__=='__main__':
    main()
