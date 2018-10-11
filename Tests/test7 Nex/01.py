n = int(input())
p = int(input())
num_list = []
for i in range(1, n+1):
    if n%i == 0:
        num_list.append(i)

if p-1 >= len(num_list):
    print(0)
else:
    print(num_list[p-1])
