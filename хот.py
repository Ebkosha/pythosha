a = [int(x) for x in input().split()]
m, k = [int(x) for x in input().split()]
print(sum(a[m:k + 1]))