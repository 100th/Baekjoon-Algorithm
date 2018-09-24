N, K = map(int, input().split())

money_list = []
for i in range(N):
    money_list.append(int(input()))

money = K
count = 0


for i in range(len(money_list)):
    count += int(money / money_list[len(money_list) - 1 - i])
    money = money % money_list[len(money_list) - 1 - i]
    if money == 0:
        break

print(count)
