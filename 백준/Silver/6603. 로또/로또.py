import itertools

while True:
    N, *lst = map(int, input().split())
    if N == 0:
        break

    combinations = list(itertools.combinations(lst, 6))
    for combi in combinations:
        print(*combi)

    print()