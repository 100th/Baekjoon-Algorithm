N = int(input())
num = input().split()


sosu_result = 0
for i in num:
    sosu_count = 0
    for j in range(1, int(i) + 1):
        if int(i) % j == 0:
            sosu_count += 1
    if sosu_count == 2: # 소수 판별
        sosu_result += 1     # 소수 개수+1
print(sosu_result)
