# 최대 상금
import sys
sys.stdin = open("input.txt", "r")

def dfs(cnt):
    global answer
    joined = ''.join(number)
    state = (joined, cnt)
    if state in visited:
        return
    visited.add(state)

    if cnt == c:
        if int(joined) > answer:
            answer = int(joined)
        return

    for i in range(len(number) - 1):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            dfs(cnt + 1)
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, T+1):
    number, c = input().split()
    number = list(number)
    c = int(c)
    answer = 0
    visited = set()
    dfs(0)
    print(f"#{tc} {answer}")