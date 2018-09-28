n = int(input())
n_list = [-1 for i in range(1000001)]
n_list[1] = 0
n_list[2] = 1
n_list[3] = 1
c = 4

while c <= n:
    v = 999999
    if c%3==0:
        t = n_list[int(c/3)]
        if v > t:
            v = t

    if c%2==0:
        t = n_list[int(c/2)]
        if v > t:
            v = t
    t = n_list[c-1]

    if v > t:
        v = t
    n_list[c] = v + 1
    c += 1

print(n_list[c-1])
