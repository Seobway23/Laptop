n = int(input())
number = 1

for i in range(2, n + 1):
    number *= i

STR = str(number)
cnt = 0
for j in range(len(STR)-1, -1, -1):
    if STR[j] == "0":
        cnt += 1
    else:
        break

print(cnt)