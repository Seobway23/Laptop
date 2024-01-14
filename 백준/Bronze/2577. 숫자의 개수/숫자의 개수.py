ans = [0] * 10
lst = list(int(input()) for _ in range(3))

cnt = 1
for i in lst:
    cnt *= i

for i in str(cnt):
    ans[int(i)] += 1

for i in ans:
    print(i)
