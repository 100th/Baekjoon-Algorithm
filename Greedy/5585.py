money = 1000 - int(input())
count = 0

count += int(money / 500)
money = money % 500

count += int(money / 100)
money = money % 100

count += int(money / 50)
money = money % 50

count += int(money / 10)
money = money % 10

count += int(money / 5)
money = money % 5

count += int(money / 1)
money = money % 1

print(count)
