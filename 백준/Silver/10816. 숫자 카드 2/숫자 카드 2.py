plus = [0] * 10000001
minus = [0] * 10000001

n = int(input())
n_lst = list(map(int, input().split()))

for i in n_lst:
    if i >= 0:
        plus[i] += 1
    else:
        minus[i] += 1

m = int(input())
m_lst = list(map(int, input().split()))

ans = []
for i in m_lst:
    if i >= 0:
        ans.append(plus[i])
    else:
        ans.append(minus[i])
print(*ans)