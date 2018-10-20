input_list = list(map(float, input().split()))

money = input_list[0]
benefit = input_list[1]
years = input_list[2]

result = money * ((1 + (benefit / 100 ))) ** years

print(format(result, "10.2f"))
