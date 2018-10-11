original = 20000

move_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(move_list)):
    if move_list[i] >= 4 and move_list[i] <= 178:
        if move_list[i] <= 40:
            if original < 40:
                break
            else:
                original -= 720
        else:
            temp = ((move_list[i] - 41)//8 + 1 ) * 80
            if original < temp + 720:
                break
            else:
                original -= temp + 720
    else:
        break

print(original)
