T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    #가로
    for i in range(N):
        count = 0
        for j in range(N):
            if board[i][j] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1
    
    #세로
    for j in range(N):
        count = 0
        for i in range(N):
            if board[i][j] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1
    print(answer)

    