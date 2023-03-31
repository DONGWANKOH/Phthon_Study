def isValid(x,y,n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False
def canBuildPillow(i,j,build):
    if j == len(build)-1:
        return False
    # 기둥의 조건
    # 바닥 위에 있거나
    if j == 0:
        return True
    # 보의 한쪽 끝 부분 위에 있거나 또 다른 기둥 위에 있어야 한다.
    if isValid(i-1,j,len(build)):
        if build[i-1][j] == 1 or build[i-1][j] == 2:
            return True
    #  또 다른 기둥 위에 있어야 한다.
    if isValid(i,j-1,len(build)):
        if build[i][j-1] == 0 or build[i][j-1] == 2:
            return True
    # ----
    if isValid(i,j,len(build)):
        if build[i][j] == 1 or build[i][j] == 2:
            return True
    return False # 통과 못함
def canBuildBeam(i,j,build):
    # 맨 오른쪽인 경우
    if i == len(build)-1:
        return False
    # 한쪽 끝 부분이 기둥 위에 있거나
    if isValid(i,j-1,len(build)):
        if build[i][j-1] == 0 or build[i][j-1] == 2:
            return True
    if isValid(i+1,j-1,len(build)):
        if build[i+1][j-1] == 0 or build[i+1][j-1] == 2:
            return True
    # 양쪽 끝 부분이 다른 보와 동시에 연결되어있어야 한다.
    if isValid(i-1,j,len(build)) and (build[i-1][j] == 1 or build[i-1][j] == 2) and isValid(i+1,j,len(build)) and (build[i+1][j] == 1 or build[i+1][j] == 2):
        return True
    return False

def isPossible(build):
    for i in range(len(build)):
        for j in range(len(build)):
            if build[i][j] == -1:
                continue
            else: # 보나 기둥이 있는 경우
                if build[i][j] == 0: # 기둥인 경우
                    if not canBuildPillow(i,j,build):
                        return False

                if build[i][j] == 1: # 보인 경우
                    if not canBuildBeam(i,j,build):
                        return False
                if build[i][j] == 2: # 둘다 설치
                    if not canBuildPillow(i,j,build):
                        return False
                    if not canBuildBeam(i,j,build):
                        return False
    return True

def solution(n, build_frame):
    beam
    build = [[-1 for i in range(n+1)] for i in range(n+1)]

    for i in range(len(build_frame)):
        x,y,a,b = build_frame[i][0],build_frame[i][1],build_frame[i][2],build_frame[i][3]

        # 이전값 저장
        tmp = build[x][y]

        if b == 0: # 삭제
            if build[x][y] == 2:
                if a == 0:
                    build[x][y] = 1
                if a == 1:
                    build[x][y] = 0
            else:
                build[x][y] = -1

        if b == 1: # 생성
            if build[x][y] == -1:
                build[x][y] = a
            else:
                build[x][y] = 2

        if not isPossible(build):
            build[x][y] = tmp
            #print(str(x)+str(y),str(a)+"설치안함")
    answer = []

    for i in range(len(build)):
        for j in range(len(build)):
            if build[i][j] == 0 or build[i][j] == 1:
                answer.append([i,j,build[i][j]])
            if build[i][j] == 2:
                answer.append([i,j,0])
                answer.append([i,j,1])

    return answer