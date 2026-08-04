T = int(input())
for test_case in range(1, T+1):
    board = [input().split() for _ in range(9)]
    answer = 1
    # 행 검사
    for i in range(9):
        if len(set(board[i])) != 9:
            answer = 0
            break
	# 열 검사
    if answer:
        for j in range(9):
            temp = []
            for i in range(9):
                temp.append(board[i][j])
            if len(set(temp)) != 9:
                answer = 0
                break
	# 네모 검사
    if answer:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                temp = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        temp.append(board[k][l])
                if len(set(temp)) != 9:
                    answer = 0
                    break
            if answer == 0:
                break
    
    print(f"#{test_case} {answer}")

# 개선점
# 열 검사에서 zip 활용
# for col in zip(*board):
#     if len(set(col)) != 9:
#         answer = 0