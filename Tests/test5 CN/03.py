n = int(input())

input_list = []
for i in range(n):
    input_list.append(list(map(int, input().split())))

visit_list = [[]]

for i in range(len(input_list[0])):
    visit_list[0].append(input_list[0][i])

for i in range(1, n):
    need_new = True
    for j in range(len(input_list[i])):
        for k in range(len(visit_list)):
            if input_list[i][j] in visit_list[k]:
                need_new = False
            else:
                visit_list[k].append(input_list[i][j])
        visit_list[k].sort()

    if need_new == True:
        visit_list.append([])
        for j in range(len(input_list[i])):
            visit_list[-1].append(input_list[i][j])
        visit_list[-1].sort()

print(visit_list)
for i in range(len(visit_list)):
    print(max(visit_list[i]))
