n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    address, password = input().split()
    dic[address] = password

for _ in range(m):
    target = input()
    print(dic[target])