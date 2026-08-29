T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]
    answer = False
    def check():
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'o':
                    for k in range(4):
                        cnt = 1
                        nx = i + dx[k]
                        ny = j + dy[k]
                        for _ in range(4):
                            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                                cnt += 1
                                nx += dx[k]
                                ny += dy[k]
                            else:
                                break
                        if cnt == 5:
                            answer = True
                            return answer
    if check():
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")