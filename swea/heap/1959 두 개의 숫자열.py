T = int(input())
for test_case in range(1, T+1):
    temp_N, temp_M = map(int, input().split())
    if temp_N > temp_M:
        N = temp_M
        M = temp_N
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
    else:
        N = temp_N
        M = temp_M
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    answer = [0] * (M-N+1)
    diff = 0
    for t in range(M-N+1):
        for i in range(N):
            answer[t] += A[i] * B[i + diff]
        diff += 1
    print(answer)