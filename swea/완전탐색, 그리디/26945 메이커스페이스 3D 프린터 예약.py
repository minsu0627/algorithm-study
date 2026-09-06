# 메이커스페이스 3D 프린터 예약

import sys
sys.stdin = open("input.txt", "r")

# 시간초과
# def cnt(temp, idx, end_time):
#     answer[0] = max(answer[0], temp)
#
#     if idx == N:
#         return
#
#     if reservations[idx][0] >= end_time:
#         cnt(temp + 1, idx + 1, reservations[idx][1])
#
#     cnt(temp, idx + 1, end_time)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     reservations = sorted([list(map(int, input().split())) for _ in range(N)])
#     answer = [0]
#
#     for i in range(N):
#         cnt(1, i+1, reservations[i][1])
#
#     print(f"#{tc} {answer[0]}")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    reservations = [list(map(int, input().split())) for _ in range(N)]
    reservations = sorted(reservations, key=lambda x:(x[1], x[0]))

    answer = 0
    end_time = 0

    for s, e in reservations:
        if s >= end_time:
            answer += 1
            end_time = e
    print(f"#{tc} {answer}")