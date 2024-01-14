r = 31
m = 1234567891

n = int(input())
STR = input()

ans = 0
for i in range(len(STR)):
    ans += (ord(STR[i]) - 97 + 1) * (r ** i)

print(ans % m)