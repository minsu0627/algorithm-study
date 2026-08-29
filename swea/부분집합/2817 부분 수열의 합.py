def dfs(idx, temp):
    temp += arr[idx]
    if temp == K:
        answer[0] += 1
        return
    elif temp > K:
        return
    for j in range(idx + 1, N):
        dfs(j, temp)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = [0]
    for i in range(N):
        dfs(i, 0)
    print(f"#{test_case} {answer[0]}")
