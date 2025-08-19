n, d, k, c = map(int, input().split())
# 1. arr 순회 => % n => 0부터 len(arr) 순회 인덱스 처리 => 그냥 2배 해주면 됨
arr = list(int(input()) for _ in range(n))
arr = arr + arr
ans = 0


for i in range(len(arr)//2):
    temp_list = arr[i:i + k]

    # 2. k번째 선택한 초밥이 모두 다른 종류 이면서, c 가 있으면 안됨
    if c not in temp_list:
        temp_list += [c]

    # 중복 처리
    set_list = set(temp_list)

    # 3. ans 갱신
    if ans < len(list(set_list)):
        ans = len(set_list)

print(ans)

