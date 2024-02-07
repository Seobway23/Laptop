n = input()

cnt = 0
for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        cnt += 1

# 뒤집은 횟수 -> 반 개
print( (cnt + 1) // 2 )