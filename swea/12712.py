T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cx = [-1, 1, 1, -1]
    cy = [1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            # plus
            temp = board[i][j]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                for _ in range(M):
                    if 0 <= nx < N and 0 <= ny < N:
                        print(board[nx][ny])
                        temp += board[nx][ny]
                    nx += dx[d]
                    ny += dy[d]
            answer = max(answer, temp)

            # cross
            temp = board[i][j]
            for d in range(4):
                nx = i + cx[d]
                ny = j + cy[d]
                for _ in range(M):
                    if 0 <= nx < N and 0 <= ny < N:
                        temp += board[nx][ny]
                    nx += cx[d]
                    ny += cy[d]
            answer = max(answer, temp)

    print(answer)