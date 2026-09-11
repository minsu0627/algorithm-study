def dfs(idx, temp):
    global answer
    if temp > K:
        return

    if temp == K:
        answer += 1
        return

    for i in range(idx, N):
        dfs(i+1, temp + nums[i])

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = 0
    dfs(0, 0)
    print(f"#{tc} {answer}")