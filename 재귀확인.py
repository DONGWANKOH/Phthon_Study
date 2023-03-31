def recursive_function(i):
    if i==10:
        return
    print(i,'번째에서',i+1,'을 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 종료')

recursive_function(1)