t = int(input())
if t >= 1 and t <= 1000:
    sum = 0
    for i in range(t):
        a, b = map(int, input().split())
        if a <= 100 and a >= 0:
            if a == 0:
                money = 0
            elif a == 1:
                money = 5000000
            elif a <= 3:
                money = 3000000
            elif a <= 6:
                money = 2000000
            elif a <= 10:
                money = 500000
            elif a <= 15:
                money = 300000
            elif a <= 21:
                money = 100000
            else:
                money = 0
            sum += money
        else:
            money = 0

        if b <= 64 and b >= 0:
            if b == 0:
                money = 0
            elif b == 1:
                money = 5120000
            elif b <= 3:
                money = 2560000
            elif b <= 7:
                money = 1280000
            elif b <= 15:
                money = 640000
            elif b <= 31:
                money = 320000
            else:
                money = 0
            sum += money
        else:
            money = 0
        print(sum)
        sum = 0
else:
    False
