def bfs():
    while q:
        global x
        x = q.pop(0)
        if x == y:
            print(visit[x])
            break
        if 100000 >= x-1 >= 0 == visit[x-1]:
            visit[x-1] = visit[x] + 1
            q.append(x-1)
        if 100000 >= x+1 >= 0 == visit[x+1]:
            visit[x+1] = visit[x] + 1
            q.append(x+1)
        if 100000 >= x*2 >= 0 == visit[x*2]:
            visit[x*2] = visit[x] + 1
            q.append(x*2)

x, y = map(int, input().split())
visit = [0] * 100001
q = [x]

bfs()
