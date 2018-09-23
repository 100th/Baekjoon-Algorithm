visit = {}
visit2 = {}
load = {}
result = []

N, M, V = map(int,input().split())
# 간선수

for i in range(M):
    start, end = map(int,input().split())

    visit[start] = visit.get(start,0)
    visit[end] = visit.get(end, 0)
    if load.get(start)==None:
        load[start]=[]
    if load.get(end) == None:
        load[end] = []
    load[start].append(end)
    load[end].append(start)
# print(visit)
# print(load)

for a in load:
    load[a].sort()
visit2=visit.copy()

def DFS(visit, load, start):
    if visit[start]==1:
        return
    visit[start]=1
    result.append(start)
    for next in load.get(start,[]):
        DFS(visit,load,next)

DFS(visit,load,V)
#print(result)
r=''
for s in result:
    r+=str(s)+' '
print(r.rstrip())

result=[]

def BFS(visit, load, stack):
    tmp = []
    for n in stack:
        if visit[n] == 1:
            continue
        visit[n]=1
        result.append(n)
        for nn in load.get(n,[]):
            if visit[nn] != 1 and nn not in tmp:
                tmp.append(nn)

    if len(tmp)==0:
        return
    BFS(visit, load,tmp)

BFS(visit2,load,[V])
#print(result)

r=''
for s in result:
    r+=str(s)+' '
print(r.rstrip())
