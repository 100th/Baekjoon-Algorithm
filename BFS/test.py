T=int(input())
maze=[]
visited=[]
for i in range(T):
    visited.append([0]*T)
dic={}
for k in range(T):
    a=list(map(int, input().split()))
    maze.append(a)
    dic[k]=dic.get(k, [])
    for idx, i in enumerate(a):
        if i==1:
            dic[k].append(idx)
