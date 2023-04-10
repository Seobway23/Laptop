import sys
sys.stdin = open('input.txt', 'r')


def divided(arr):
    #종료조건: 재귀함수의 처음은 종료 조건
    if len(arr) == 1:
        return arr

    # 절반 나눠서 양쪽 정렬
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    # 내가 바꾼 값들을 변수 할당을 통해 변화를 주어야 정렬됨
    left = divided(left)
    right = divided(right)
    return merge(left, right)


def merge(l, r):
    global cnt
    merge_lst = []
    i = j = 0

    #문제 조건 cnt 세기
    if l[-1] > r[-1]:
        cnt += 1

    while i < len(l) and j < len(r):
        #print('i:', i, 'j:', j, 'l:', l , 'r:', r)

        if l[i] < r[j]:
            merge_lst.append(l[i])
            i += 1

        else:
            merge_lst.append(r[j])
            j += 1

    merge_lst += l[i:] + r[j:]
    #print('merge_lst:', merge_lst)
    return merge_lst


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = divided(arr)
    #print(ans)
    print(f"#{test_case} {ans[N//2]} {cnt}")
