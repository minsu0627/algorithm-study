# import sys
# sys.stdin = open("input.txt", "r")

def dfs(r, c, cnt):
    global answer, joker
    answer = max(answer, cnt)

    height = mountain[r][c]

    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if mountain[nr][nc] < height:
                visited[nr][nc] = True
                dfs(nr, nc, cnt + 1)
                visited[nr][nc] = False
            else:
                if not joker:
                    for minus in range(1, K + 1):
                        temp_height = mountain[nr][nc]
                        if temp_height - minus < height:
                            joker = True
                            mountain[nr][nc] = temp_height - minus
                            visited[nr][nc] = True
                            dfs(nr, nc, cnt + 1)
                            joker = False
                            mountain[nr][nc] = temp_height
                            visited[nr][nc] = False
                            break

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    highest = 0
    highest_info = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > highest:
                highest = mountain[i][j]
                highest_info.clear() # 초기화
                highest_info.append((i, j))
            elif mountain[i][j] == highest:
                highest_info.append((i, j))

    visited = [[False] * N for _ in range(N)]
    answer = 0
    joker = False

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for info in highest_info:
        hr, hc = info[0], info[1]
        visited[hr][hc] = True
        dfs(hr, hc, 1)
        visited[hr][hc] = False

    print(f"#{tc} {answer}")