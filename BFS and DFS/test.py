from sys import*
setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

vertical,horizontal,unit = map(int,input().strip().split())

input_list = [[0]*horizontal for i in range(vertical)]

visit = [[True]*horizontal for i in range(vertical)]

for i in range(unit):
    x1,y1,x2,y2 = map(int,input().strip().split())
    for ver in range((vertical-y2),(vertical-y1),1):
        for hor in range(x1,x2,1):
            input_list[ver][hor]=1

def dfs(y,x):
    global val
    val+=1
    visit[y][x] = False     # 방문한다

    for i in range(4):
        dir_y = y + dy[i]
        dir_x = x + dx[i]
        if dir_x > -1 and dir_x < horizontal and dir_y > -1 and dir_y < vertical:
            if visit[dir_y][dir_x] == True and input_list[dir_y][dir_x] == 0: # 온적이 없다면
                dfs(dir_y,dir_x)            # DP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

result = []
for i in range(vertical):
    for j in range(horizontal):
        if visit[i][j] == True and input_list[i][j] == 0:  # 온적이 없다면
            val = 0
            dfs(i,j)
            result.append(val)

print(len(result))
for i in sorted(result):
    print(i,end=" ")
