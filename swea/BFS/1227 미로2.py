# 미로2
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs():
    global found

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == end_x and ny == end_y:
                found = True
                return
            elif 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and board[nx][ny] != '1':
                if board[nx][ny] == '0':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return

for _ in range(10):
    tc = int(input())
    board = [list(input()) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == '2':
                start_x, start_y = i, j
            elif board[i][j] == '3':
                end_x, end_y = i, j

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    found = False

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    bfs()
    if found:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")