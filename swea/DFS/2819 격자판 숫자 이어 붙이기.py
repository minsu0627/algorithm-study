import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c, num):
    if len(num) == 7:
        answer.add(num)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, num + board[nr][nc])

T = int(input())
for tc in range(1, T+1):
    board = [input().split() for _ in range(4)]
    answer = set()

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(4):
        for j in range(4):
            dfs(i, j, '')

    print(f"#{tc} {len(answer)}")