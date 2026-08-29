def check_point(idx):
    point = 0
    for i in range(idx + 1, N):
        if books[idx] > books[i]:
            point += 1
    return point

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    books = list(map(int, input().split()))
    max_num = 0
    max_height = check_point(0)
    for i in range(1, N):
        if books[i] > books[max_num]:
            compare_num = check_point(i)
            if compare_num > max_height:
                max_num = i
                max_height = compare_num
    print(f"#{test_case} {max_height}")

