import sys
sys.stdin = open('input.txt')

'''
1. input

2. 움직임
1) 가장 위에 물고기
2) 가장 왼쪽 물고기
3) ans += 1 -> 최종 출력 -> 시간

3. shark
1) size
2) eat
'''

# input
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#