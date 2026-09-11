# 햄버거 다이어트
def dfs(idx, point, cal):
    global answer
    if cal > L:
        return

    answer = max(answer, point)

    for i in range(idx, N):
        dfs(i + 1, point + info[i][0], cal + info[i][1])

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dfs(0, 0, 0)
    print(f"#{tc} {answer}")