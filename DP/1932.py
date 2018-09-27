N = int(input())
tri = [0] * N

for i in range(N):
    tri[i] = list(map(int, input().split()))

for i in range(1, N):
    for j in range(len(tri[i])):
        if j == 0:  # 맨 왼쪽은 그냥 더하기
            tri[i][j] += tri[i-1][0]
        elif j == i:    # 맨 오른쪽도 그냥 더하기
            tri[i][j] += tri[i-1][j-1]
        else:   # 그 외
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[N-1]))
