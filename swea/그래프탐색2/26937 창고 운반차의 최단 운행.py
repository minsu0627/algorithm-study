# 창고 운반차의 최단 운행
import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def bfs():
    count = 0
    queue = deque([(start_x, start_y, count)])
    visited[start_x][start_y] = True

    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == '3':
                    print(f"#{test_case} {cnt}")
                    return
                elif board[nx][ny] == '0' and not visited[nx][ny]:
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True

    print(f"#{test_case} 0")
    return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    start_x, start_y = 0, 0
    visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] == '2':
                start_x, start_y = r, c

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    bfs()
