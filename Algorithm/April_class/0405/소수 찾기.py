import sys
sys.stdin= open('input.txt', 'r')

T = int(input())
lst = list(map(int, input().split()))
ans = 0
'''
1. N개 입력 중 소수의 갯수는?
소수가 뭐임?
약수가 1과 자기 자신만 포함하는 수

여집합을 해보면 ->  1과 자기자신이 아닌 모든 숫자에 나누어떨어지지 않으면 됨.
'''

for i in lst:
    cnt = 0
    if i != 1: # 1은 소수가 아니기 때문에 1을 제외해야 함
        for j in range(2, i): # 2부터 i-1까지
            if i%j == 0:
                cnt += 1    # 스위치, 범위내 나누어떨어지면, cnt += 1
                            # cnt =1 을 하면, 새로운 주소에 할당해야 하기 때문

        if cnt ==0:
            ans += 1

print(ans)