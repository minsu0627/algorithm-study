def dfs(idx, taste, kcal):
    taste += info[idx][0]
    kcal += info[idx][1]

    if kcal > L:
        return

    if taste > answer[0]:
        answer[0] = taste

    for j in range(idx + 1, N):
        dfs(j, taste, kcal)

T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    answer = [0]
    for i in range(N):
        dfs(i, 0, 0)
    print(f"#{test_case} {answer[0]}")

# =====================================
# DP
# =====================================
T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())

    dp = [0] * (L+1)

    for _ in range(N):
        taste, kcal = map(int, input().split())

        for j in range(L, kcal-1, -1):
            if dp[j-kcal] + taste > dp[j]:
                dp[j] = dp[j-kcal] + taste
    print(f"#{test_case} {max(dp)}")