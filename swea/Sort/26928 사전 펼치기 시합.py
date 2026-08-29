def page_count(target):
    l = 1
    r = P
    c = int((l+r)/2)
    count = 0
    while True:
        count += 1
        if target == c:
            break

        if target > c:
            l = c
        else:
            r = c
        c = int((l+r)/2)
    return count

T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    A_count = page_count(A)
    B_count = page_count(B)
    if A_count < B_count:
        print(f"#{test_case} A")
    elif A_count > B_count:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")