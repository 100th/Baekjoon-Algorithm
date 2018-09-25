N = int(input())

rope_list = []
for i in range(N):
    rope_list.append(int(input()))

rope_list.sort(reverse=True)

max = rope_list[0]
for i in range(1, N):
    temp_max = rope_list[i] * (i + 1)
    if temp_max > max:
        max = temp_max

print(max)
