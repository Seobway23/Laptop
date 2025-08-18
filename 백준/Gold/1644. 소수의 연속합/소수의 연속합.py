n = int(input())

is_prime = bytearray(b"\x01") * (n + 1)
is_prime[0:2] = b"\x00\x00"

p = 2
while p * p <= n:
    if is_prime[p]:
        start = p * p
        step = p
        is_prime[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
    p += 1

primes = [i for i in range(2, n + 1) if is_prime[i]]

start, cur = 0, 0
cnt = 0

for end in range(len(primes)):
    cur += primes[end]

    # start 는 end 를 넘어갈 수 없음
    # n이 더 크다면, 빼기 위해서 start 증가
    while cur > n and start <= end:
        # start 갱신
        cur -= primes[start]
        start += 1

    if cur == n:
        cnt += 1
        cur -= primes[start]
        start += 1

print(cnt)