n = int(input())
ans = 0

for i in range(1, n + 1): # 1부터 n까지
    sm_num = sum(map(int, str(i))) # 각 자리수 합 구하기
    sm_total = i + sm_num
    
    if sm_total == n:
        ans = i
        break

print(ans)