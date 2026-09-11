# 동철이의 일 분배
import sys
sys.stdin = open('input.txt', 'r')

def dfs(worker_num, success):
    if success <= answer[0]:
        return

    if worker_num == N and success > answer[0]:
        answer[0] = success

    for i in range(N):
        if done[i]:
            continue
        else:
            done[i] = True
            dfs(worker_num+1, success * (work[worker_num][i])/100)
            done[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    done = [False] * N
    answer = [0]
    dfs(0, 1)
    print(f"#{tc} {answer[0]*100:.6f}")