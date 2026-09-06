# 삼색 칩 대회
# def judge(A, B):
#     winner = A
#     if A[1] == B[1]:
#         if A[0] > B[0]:
#             winner = B
#     elif B[1] == 1 and A[1] == 3:
#         winner = B
#     elif B[1] == 2 and A[1] == 1:
#         winner = B
#     elif B[1] == 3 and A[1] == 2:
#         winner = B
#     return winner
#
# def match(line):
#     if len(line) == 1:
#         return line[0]
#     temp = []
#     for j in range(0, len(line), 2):
#         if j + 1 == len(line):
#             temp.append(line[j])
#             break
#         temp.append(judge(line[j], line[j + 1]))
#     return match(temp)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     temp_chips = list(map(int, input().split()))
#     chips = []
#     for i in range(1, N+1):
#         chips.append([i, temp_chips[i-1]])
#     print(f"#{tc} {match(chips)[0]}")

def judge(A, B):
    winner = A
    if A[1] == B[1]:
        if A[0] > B[0]:
            winner = B
    elif B[1] == 1 and A[1] == 3:
        winner = B
    elif B[1] == 2 and A[1] == 1:
        winner = B
    elif B[1] == 3 and A[1] == 2:
        winner = B
    return winner

def match(start, end, line):
    if start == end:
        return line[start]

    mid = (start + end) // 2

    left_winner = match(start, mid, line)
    right_winner = match(mid+1, end, line)
    return judge(left_winner, right_winner)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp_chips = list(map(int, input().split()))
    chips = []
    for i in range(1, N+1):
        chips.append([i, temp_chips[i-1]])
    print(f"#{tc} {match(0, len(chips)-1, chips)[0]}")