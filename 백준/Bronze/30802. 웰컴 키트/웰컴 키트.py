n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum( (i + t - 1) // t for i in arr))
print(n // p, n % p)