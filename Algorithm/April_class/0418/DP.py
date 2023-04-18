# DP는 기존의 DFS, BFS의 방식을 효과적으로 연산 속도를 빠르게 하기 위함
# 여기에서는 인덱스 활용을 통해 연산 속도 감소



def fib(n):
    global cnt
    if n==1 or n==2:
        cnt += 1
        return 1
    else:
        fib(n-1)
        fib(n-2)
    

def fibonacci(n):
    global ans, f
    f = [0]*(n+1)
    f[1] = 1
    f[2] = 1
    
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        ans += 1

ans = 0
cnt = 0
n = int(input())
fib(n)
fibonacci(n)
print(cnt, ans)