import math

N, K = map(int, input().split())

a = []
a = list(map(int, input().split()))

min_boon_sum = 1000000000

for q in range(len(a) - K + 1):
    sum = 0
    mean = 0
    for r in range(q, K + q):
        sum += int(a[r])
    mean = float(sum/K)

    boon_sum = 0

    for q in range(q, K + q):
        boon_sum += pow((int(a[q]) - mean), 2)

    if boon_sum < min_boon_sum:
        min_boon_sum = boon_sum

boonsan = min_boon_sum/K

print(round(math.sqrt(boonsan), 15))
