a, b = map(str, input().split())

chai_list = []
for j in range(len(b)-len(a)+1):
    chai = 0
    for k in range(len(a)):
        if b[j+k] != a[k]:
            chai += 1
    chai_list.append(chai)

if len(chai_list) == 0:
    print(0)
else:
    print(min(chai_list))
