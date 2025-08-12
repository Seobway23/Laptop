# init
n = int(input())
arr = [int(input()) for _ in range(n)]

# sort
arr.sort(reverse=True)
ans = 0

# logic
for i, w in enumerate(arr, start = 1):
    ans = max(ans, w * i)

print(ans)