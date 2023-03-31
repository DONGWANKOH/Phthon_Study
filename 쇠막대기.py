import sys
read = sys.stdin.readline
# ()(((()())(())()))(())
#괄호인 경우 Stack을 의심한다.


stick = sys.stdin.readline().strip()
stack = []
result = 0
pre = ""
for i in stick:
    if i == "(":
        stack.append(i)

    else:
        # stack.pop() #아래에서 코드 중복을 피하기 위하여 추가한다.
        if i == ")" and pre == "(":
            stack.pop()  #레이저라면 앞에 ( 추가한거는 pop을 하고 숫자 세기
            result += len(stack)
        elif i == ")" and pre == ")":
            stack.pop()  #레이저가 아닌 경우 pop이 중복되었다..
            result += 1
    pre = i
print(result)
###############정답코드######################
import sys
read = sys.stdin.readline


def main():
    stick = read().rstrip()
    stack = []
    res = 0

    for i in range(len(stick)):
        if stick[i] == '(':    # 여는 괄호는 무조건 넣어야 됨.
            stack.append('(')
            continue    # else 쓰면 들여쓰기가 많이 되어서 피하기 위함
        # 이제부터는 닫는 괄호만 생각하면 됨. 문제 특성 상 문자열의 첫번째 문자가 ')' 일 수가 없으므로 고려할 필요 없음
        stack.pop()     # 닫는 괄호가 나오면 pop해야 함. 그래야 레이저일 경우 size만으로 잘린 막대의 개수를 셀 수 있음
        if stick[i - 1] == '(':     # 바로 이전에 여는 괄호가 나왔으면 레이저. 이때는 잘린 막대의 왼쪽을 계산하는 개념
            res += len(stack)
        else:   # 바로 앞이 여는 괄호가 아니기 때문에 막대기가 끝나는 부분. 끝났으므로 +1을 하여 그 막대기에 대한 연산을 마무리
            res += 1

    print(res)


if __name__ == '__main__':
    main()

'''
def main():
    bar = list(read())
    stack=[]
    stack_new=[]
    res=0

    stack.append(bar[0])
    stack_new.append(bar[0])
    for i in range(1,len(bar)):
        if bar[i-1]=='(' and bar[i]==')':
            res+=len(stack[:i-1])

        elif bar[i - 1] == ')' and bar[i] == ')':
            res += 1
            stack.append(bar[i])
            stack_new.append(bar[i])

        elif bar[i - 1] == '(' and bar[i] == '(':
            # res += 1
            stack.append(bar[i])
            stack_new.append(bar[i])
        elif len(stack_new)==0:
            stack.append(bar[i])
            stack_new.append(bar[i])
        elif bar[i - 1] == ')' and bar[i] == '(':
            res += len(stack[:i - 1])
            stack=[]

        if stack_new[-1] == '(' and bar[i] == ')':
            stack_new.pop()
        else :
            stack_new.append(bar[i])


        print(stack,stack_new, res)
        # else:
        #     stack.append(i)

    print(res)



if __name__ == '__main__':
    main()
    
'''