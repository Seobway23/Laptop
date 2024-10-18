from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int( n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            num_set.add(num)
    
    for num in num_set:
        if is_prime(num):
            answer += 1
    
    return answer