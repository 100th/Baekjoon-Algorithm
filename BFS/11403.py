N = int(input())
inputMap = []
for i in range(N):
    inputMap.append([0] * N)

for i in range(N) :
    for j, m in enumerate(map(int, input().split())) :
        inputMap[i][j] = m

#플로이드 워셜 알고리즘(Floyd Warshall Algorithm) 이용
for a in range(N):
    for b in range(N):
        for c in range(N):
            if inputMap[b][a] and inputMap[a][c]:
                inputMap[b][c] = 1

for i in range(0, N) :
    _str = ""
    for j in range(0, N) :
        _str += str(inputMap[i][j]) +  " "
    print(_str)
