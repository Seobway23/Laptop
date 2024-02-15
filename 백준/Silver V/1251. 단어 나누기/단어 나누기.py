
n = list(input())
ans, tmp = [], []

for i in range(1, len(n)-1):
    for j in range(i + 1, len(n)):
        a = n[:i]
        b = n[i:j]
        c = n[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)

for t in tmp:
    ans.append(''.join(t))

print(sorted(ans)[0])