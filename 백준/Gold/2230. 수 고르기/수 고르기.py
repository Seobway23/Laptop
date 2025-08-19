n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort()
ans = float('inf')
left, right = 0, 1

while left <= right < n:
    # m 보다 작으면 right + 1
    if arr[right] - arr[left] < m:
        right += 1

    # m보다 크거나 같으면
    else:
        # 갱신
        ans = min(ans, arr[right] - arr[left])
        left += 1

print(ans)