T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    first = input().split()
    second = input().split()
    answer = 0
    if N > M:
        N, M = M, N
        first, second = second, first
    first = set(first)
    for w in second:
        if w in first:
            answer += 1
    print(f"#{test_case} {answer}")