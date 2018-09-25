n, m, k = map(int, input().split())

maxTeamCount = 0

# 대회에 나갈 조건을 생각하기
while m+n >= k + 3 and n >= 2 and m >= 1:
    maxTeamCount += 1
    m -= 1
    n -= 2

print(maxTeamCount)
