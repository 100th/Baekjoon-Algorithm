def step(x,y):
    global arr
    global visited
    global count
    p = [(1,3,6,7),(1,3,4,5),(1,2,4,7),(1,2,5,6)] # EWSN
    possible1 =p
    possible2 = [(),(),p[2],p[3]]
    possible3 = [p[0],p[1],(),()]
    possible4 = [p[0],(),(),p[3]]
    possible5 = [p[0],(),p[2],()]
    possible6 = [(),p[1],p[2],()]
    possible7 = [(),p[1],(),p[3]]
    possible = [possible1,possible2,possible3,possible4,possible5,possible6,possible7]
    queue = [(x,y)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x,y=queue.pop(0)
        visited[x][y]=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny]!=1 and arr[nx][ny] in possible[arr[x][y]-1][i]:
                count[nx][ny]=count[x][y]+1
                queue.append((nx,ny))


T = int(input())
for t in range(T):
    N,M,R,C,L = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    visited = [[0]*M for i in range(N)]
    count = [[0]*M for i in range(N)]
    count[R][C]=1
    step(R,C)
    sum = 0
    for i in range(N):
        for k in range(1,L+1):
            sum+=count[i].count(k)
    print('#%d %d' %(t+1,sum))
