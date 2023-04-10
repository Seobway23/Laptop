'''
0 : '0001101'
1 : '0011001'
2 : '0010011' 
3 : '0111101'
4 : '0100011'
5 : '0110001'
6 : '0101111'
7 : '0111011'
8 : '0110111'
9 : '0001011'
'''
import sys
sys.stdin = open('input.txt','r')

def arr_det(N, M, arr):
    for i in range(N):
        for j in range(M-1, 0-1, -1):
            d = arr[i][j]
            if arr[i][j] == '1':
                str1 = arr[i][j-56+1:j+1]
                return str1



T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split()) # N 세로크기, M 가로 크기
    arr = [ input() for _ in range(N)]
    dic = {'0001101': 0, '0011001': 1, '0010011': 2 , '0111101' : 3, '0100011' : 4, '0110001':5, '0101111' : 6, '0111011': 7, '0110111' : 8, '0001011' : 9 }

    #str return
    str1 = arr_det(N, M, arr)

    #str 암호필터링
    filter = []
    for k in range(0, len(str1), 7):
        dd= str1[k:k+7]
        ddd = dic[str1[k:k+7]]
        filter.append(dic[str1[k:k+7]])

    #암호 판별
    odd = 0; even = 0; #odd 홀수, even 짝수
    for i in range(len(filter)-1): #filter 검증 7자리 인덱스 0~6까지
        if i % 2 == 0:
            odd += filter[i]
        else:
            even += filter[i]

    #계산 시작/ 10의 배수라면,
    if (odd*3 + even + filter[-1] ) % 10 == 0:
        ans = 0
        for t in filter:
            ans += t

    else:
        ans = 0

    print(f"#{test_case} {ans}")



