
n = int(input())
arr = list(map(int, input().split()))

# 직관을 위해 변수로 둠
s, e = 0, len(arr) - 1
best_sum = arr[s] + arr[e]
best_abs = abs(best_sum)



# s 갱신
while s < e:
    cur  =  arr[s] + arr[e]

    # 가지 치기
    if cur == 0:
        best_sum = 0
        break

    # ans 갱신
    if abs(cur) < best_abs:
        best_abs = abs(cur)
        best_sum = cur

    # s 갱신
    if cur < 0:
        s += 1

    # e 갱신
    elif cur > 0:
        e -= 1

print(best_sum)