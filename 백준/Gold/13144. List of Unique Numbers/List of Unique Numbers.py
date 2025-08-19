n = int(input())
arr = list(map(int, input().split()))
ans = 0
right = 0
seen = [0] * 100001

# left 처리
for left in range(n):
    # right 확장, 중복 전까지
    while right < n and seen[arr[right]] == 0:
        seen[arr[right]] = 1
        right += 1

    # left 시작 , 하나씩 다 세기
    ans += right - left

    # left 중복 체크 대상 제거
    seen[arr[left]] = 0

print(ans)