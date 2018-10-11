string = " "

string = string.strip().replace('?', '.').replace('!','.').split('.')

max = 0
for i in range(len(string)):
    tmp = " ".join(string[i].split())
    mine = tmp.strip().split(' ')
    if max < len(mine):
        max = len(mine)
    print(mine)

if max == 1 and mine[0] == '':
    print(0)
else:
    print(max)
