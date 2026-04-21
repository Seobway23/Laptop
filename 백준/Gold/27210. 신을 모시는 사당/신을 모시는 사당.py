n = int(input())
arr = list(map(int, input().split()))

# 1을 +1, 2를 -1로 변환
converted = [1 if x == 1 else -1 for x in arr]

max_sum = cur_max = converted[0]
min_sum = cur_min = converted[0]

for x in converted[1:]:
    cur_max = max(x, cur_max + x)
    max_sum = max(max_sum, cur_max)

    cur_min = min(x, cur_min + x)
    min_sum = min(min_sum, cur_min)

print(max(max_sum, -min_sum))