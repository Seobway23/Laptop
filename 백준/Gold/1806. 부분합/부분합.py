n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = float('inf')
left = 0
cnt = 0

for right in range(n):
    cnt += arr[right]

    # sm을 넘을 때 ans 를 줄인다.
    while cnt >= s: # 이미 s를 넘으면 left 에서 감소
        ans = min(ans, right - left + 1)
        cnt -= arr[left]
        left += 1

print( 0 if ans == float('inf') else ans)