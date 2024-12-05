def verify(lst):
    v = [0] * n
    flag = [0] * n
    for i in range(n-1):    # i, i + 1 이므로 n-2까지만 해야 함
        # 2 이상 False
        if abs(lst[i] - lst[i + 1]) > 1:
            return False

        # 1 미만 일 때      # 3 3 3 3 2 2 일 때  for 문 돌려서 v 가 아닐 때 는
        else:
            # 내리막
            next, cur = lst[i + 1], lst[i]
            if cur > next:
                for j in range(1, L + 1):
                    ni = i + j
                    if 0<= ni < n and next == lst[ni] and not v[ni]: # 범위내, 미방문, 조건1
                        v[ni] = 1   # next 에 v = 1 해야 함
                        # print("", i,v)

                    else:
                        return False

            # 오르막
            elif cur < next:
                for j in range(0, L):
                    ni = i - j
                    if 0<= ni < n and cur == lst[ni] and not v[ni]: # 범위내, 미방문, 조건1
                        v[ni] = 1    # cur 에 v = 1 해야 함
                    else:
                        return False

    return True

n, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 가로
for lst in arr:
    if verify(lst):
        ans += 1

for lst in list(zip(*arr)):
    if verify(lst):
        ans += 1

print(ans)