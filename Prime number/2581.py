import sys

# M, N = map(int, sys.stdin.readline())
# N = int(sys.stdin.readline())
M = int(input())
N = int(input())

sosu_result = 0
sum = 0
for i in range(M, N):
    sosu_count = 0
    for j in range(1, int(i) + 1):
        if int(i) % j == 0:
            sosu_count += 1
    if sosu_count == 2: # 소수 판별
        sosu_result += 1     # 소수 개수+1e
        sum += i
    if sosu_result == 1 and sosu_count == 2:
        minimum = i

if sum == 0:
    # sys.stdout.write(-1)
    print(-1)
else:
    # sys.stdout.write(sum)
    # sys.stdout.write(minimum)
    print(sum)
    print(minimum)
