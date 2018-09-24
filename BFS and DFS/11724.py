import sys
sys.setrecursionlimit(100000)

# N : 점 개수
# M : 선 개수

N, M = map(int, sys.stdin.readline().split())

line_list = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line_list.append([a, b])

visit_list = []
for i in range(N):
    visit_list.append(False)

def DFS(z):
    visit_list[z - 1] = True
    for i in range(len(line_list)):
        if line_list[i][0] == z and visit_list[line_list[i][1] - 1] == False:
            new_z = line_list[i][1]
            DFS(new_z)

        elif line_list[i][1] == z and visit_list[line_list[i][0] - 1] == False:
            new_z = line_list[i][0]
            DFS(new_z)

value = 0
for i in range(N):
    if visit_list[i] == False:
        value += 1
        DFS(i + 1)

print(value)

# line_list
# visit_list
# input_list
