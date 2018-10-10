# 2차원 배열
# 완전 탐색

import itertools

def score(real_x,real_y,cases):
    global result
    dx = [-1,1,1,-1]    # 시계방향
    dy = [1,1,-1,-1]
    for case in cases:  # ★
        trace = [arr[real_y][real_x]]
        x = real_x
        y = real_y
        i=0
        t=1
        kk=0
        while i<4:  # 이 while 문 안에서 해답이 나온다. 시계방향으로 이동하기에.
            x = x+dx[i]
            y = y+dy[i]
            if x==real_x and y==real_y: # 제자리 오면 break
                break
            if x>=0 and x<N and y>=0 and y<N and arr[y][x] not in trace:
                trace.append(arr[y][x])
                t+=1
            else:   # 경로 이탈하거나 중복되면 break
                kk=1
                break
            if t==case[i]:  # case의 길이만큼 이동하면 i를 증가시켜 방향을 바꿈
                i+=1
                t=1 # 이동거리 다시 1로 초기화
        if kk==0:   # 성공한 것만 result에 넣기
            result.append(len(trace))


T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    case_tmp = list(range(2,N)) # 가능한 변의 크기
    case = list(itertools.product(case_tmp,repeat = 2)) # (오른쪽 방향 대각선 크기, 왼쪽 방향 대각선 크기) # 중복수열 생성
    for i in range(len(case)):  # 사각형 길이 만듦
        case[i]=case[i]+case[i]

    result = []
    for x in range(N):
        for y in range(N):
            score(x,y,case)
    if len(result)==0:
        print('#%d %d' %(t+1, -1))
    else:
        print('#%d %d' %(t+1, max(result)))

# if n = 4:
# case = [(2,2,2,2),(2,3,2,3),(3,2,3,2),(3,3,3,3)]
