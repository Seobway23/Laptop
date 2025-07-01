n = int(input())
arr = list(map(int, input().split()))

# 최소 자기 자신을 가지므로 1개로 초기화
dp = [1] * n
# 전 인덱스 표시
prev = [-1] * n

for i in range(n):
    for j in range(i):
        # 만약 증가하고, 지금보다 길다면
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j


# LIS 길이
length = max(dp)
print(length)