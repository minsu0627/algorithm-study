T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    days = [list(map(int, input().split())) for _ in range(N)]
    maximum = 1
    minimum = 10000
    for i in range(N-M):
        temp = sum(days[i:i+M])
        maximum = max(maximum, temp)
        minimum = min(minimum, temp)
    answer = maximum - minimum
    print(f"#{test_case} {answer}")