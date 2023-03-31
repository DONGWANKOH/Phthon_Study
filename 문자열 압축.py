import sys
read=sys.stdin.readline
#숫자 1은 생략-개수 하나 , 2는 개수 하나, 3은 1개 마이너스 , 4개는 2마이너스 aaaa >> 4a, 5개는 3개 마이너스

def solution(s):
    # stack=[]
    # stack.append(s[0])

    # for i in range(len(s), 0):
    #     #반복되는 숫자열의 개수가 높을 수록 반복된 수가 많을 수록 압축이 많이 된다. 따라서 거꾸로 찾아서 있으면 바로 return하기
    #     #반복 숫자열의 길이 l, 반복수 n >> ababab >>>> l:2 // 반복수 :3 합 5  >>3ab : 3글자
    #     #abcabc >>   l:3 // 반복수 2 : 합 5 >> 2abc : 4글자. 숫자는 1칸 + 글자수
    #     #하기만 abab, abab 이런 경우는? 2abab, 4ab  >> 즉 l의 길이가 >l*반복수  4<l+1(숫자자리수)
    #     if s[:i] in s[i:]:
    cnt=1
    ans=987654321
    res=[]
    for j in range(0,len(s)//2):  #반복이므로 줄이는 최대 길이는 문장의 반의 길이임>> 최소 1번 반복 시에 문자길이 반.
        for i in range(1,len(s),j+1): #len(s)//2까지 포함될 수 있도록 j+1을 진행한다.
            if s[j:j+i]==s[j+i:j+i+i]:#문자가 같으면?? #처음 문자를 계속 구함으로 시간은 좀더 오래 걸림..
            # if s[0:i] == s[j+i :j+i+i]:  # 문자가 같으면?? #처음 문자를 계속 구함으로 시간은 좀더 오래 걸림..
                cnt+=1
            else:
                continue
        res.append(cnt)
        cnt=1

    print(res[:-1]) #aaabbb >

    # for in res:
    return ans

def main():
    s=read().rstrip()
    print(solution(s))


if __name__=='__main__':
    main()