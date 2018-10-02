n=int(input())
num=[0]+list(map(int,input().split()))
sum=[num[0]]

for i in range(1,n+1):
    sum.append(max(sum[i-1]+num[i], num[i]))

print(max(sum[1:]))
