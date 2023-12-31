
def multiprint(num, str):
    ans = ""
    for i in str:
        ans += i * num

    return ans


n = int(input())

for _ in range(n):
    num, str  = input().split()
    print(multiprint(int(num), str))