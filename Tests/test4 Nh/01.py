item_list = list(map(int, input().split()))

item_stack = []
for i in range(3):
    item_stack.append(item_list[i])

pop_list = []
for i in range(3, len(item_list)):
    if item_list[i] not in item_stack:
        item_stack.append(item_list[i])
        pop_list.append(item_stack.pop(0))

    else:
        item_stack.remove(item_list[i])
        item_stack.append(item_list[i])

if len(pop_list) == 0:
    print(0)
else:
    print(pop_list)
