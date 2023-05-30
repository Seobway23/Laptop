import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int,input().split()))
B, C = map(int, input().split())
ans = 0
# cnt = 0
for i in A:
    number = i
    # 총감독 ans +1
    if number - B >= 0:

        number -= B
        ans += 1
        # print(cnt, ans, number)

        # 부감독 + 1 loop
        if number % C != 0:
            ans += number//C + 1

        else:
            ans += number//C

    else:
        ans += 1

    # cnt += 1
    # print(cnt, ans, number)
print(ans)

'''
틀릭 코딩
        # 부감독 + 1 loop
        while True:
            if number <= 0:
                break
            number -= C
            ans += 1
            # print(cnt, ans, number)

나누지 않고 그냥 더했음

'''