n = int(input())
price = list(map(int, input().split()))
max_price = [0 for i in range(n)]
max_price[0] = price[0]

for i in range(1,n):
    max_price[i] = price[i]
    for j in range(i):
        print('bread[{}] = (bread[{}] + p[{}])'.format(i,i-j,j))
        if max_price[i] < max_price[i-j-1] + price[j]:
            max_price[i] = max_price[i-j-1] + price[j]
print(max_price[n-1])
max_price
