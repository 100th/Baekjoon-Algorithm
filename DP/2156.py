n = int(input())
wine = [0]

for i in range(1, n + 1):
    temp = int(input())
    wine.append(temp)

dp = [0 for i in range(n + 1)]

if n == 1:
    dp[1] = wine[1]
else:
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])

print(dp[n])
