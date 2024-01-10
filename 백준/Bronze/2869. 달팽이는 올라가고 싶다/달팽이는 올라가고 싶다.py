import math

A, B, V = map(int, input().split())
# 올라갈 거리 V - B
# 소수점이 나올 경우 올림
print(math.ceil((V-B) / (A - B)))
