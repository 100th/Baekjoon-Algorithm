n = int(input())
k = int(input())

n = 2
k = 2
now = 0
i = 1
jump = 0

while now < k and jump <= n:
    now += i
    jump += 1
    i += 1
    if now == k:
        break

print(now)

from copy import copy
a = []
for i in range(1000):
    a.append(i)

b = copy(a)

now = 0
jump = 0
for i in range(1, len(a)):
    b.remove(i)
    for j in range(len(b)):
        now += b[j]
        if now > k:
            break

print(now)
