row, col = map(int, input().split())
map = [""] * row
print(map)
visit = [[0] * col for _ in range(row)]
print(visit)
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

dir

for i in range(row):
    map[i] = input()
