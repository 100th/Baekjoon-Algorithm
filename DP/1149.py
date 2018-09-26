n = int(input())
rgblist = []

for i in range(n):
    r, g, b = map(int, input().split(" "))
    rgblist.append([r, g, b])

dp = []

# rgblist
dp.append(rgblist[0])

# dp

for i in range(1, n):
    temp = []
    temp.append(min(dp[i-1][1], dp[i-1][2]) + rgblist[i][0]) # r을 선택했을 경우
    temp.append(min(dp[i-1][0], dp[i-1][2]) + rgblist[i][1]) # g를 선택했을 경우
    temp.append(min(dp[i-1][0], dp[i-1][1]) + rgblist[i][2]) # b를 선택했을 경우

    dp.append(temp)

# dp

print(min(dp[n - 1])) #  마지막 단계이므로 3가지 경우의 수 중 가장 작은 값을 리턴
