n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
odd_cnt = 0
ans = 0

for right in range(n):
    # 홀 수 라면
    if arr[right] % 2 == 1:
        odd_cnt += 1

        while odd_cnt > k:
            if arr[left] % 2 == 1:
                odd_cnt -= 1

            left += 1

    # ans  갱신
    cur_length = (right - left + 1 ) - odd_cnt
    ans = max(ans, cur_length)

print(ans)