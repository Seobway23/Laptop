n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
order_lst = []

for i, j in arr:
    order = 1
    # 다 비교 한 후
    for k, h in arr:
        if i < k and j < h:
            order += 1
            
    # order_lst 에 추가
    order_lst.append(order)

print(*order_lst)
