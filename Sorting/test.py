a = []
for _ in range(int(input())):
    tmp = input()
    if tmp not in a:
        a.append(tmp)
a.sort()


for i in sorting(a):
    print(i)
