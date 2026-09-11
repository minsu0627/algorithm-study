# 숫자 만들기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, cur, plus, minus, multiple, divide):
    global maximum, minimum
    if idx == N:
        maximum = max(maximum, cur)
        minimum = min(minimum, cur)
        return

    next = nums[idx]

    if plus > 0:
        dfs(idx+1, cur+next, plus-1, minus, multiple, divide)
    if minus > 0:
        dfs(idx+1, cur-next, plus, minus-1, multiple, divide)
    if multiple > 0:
        dfs(idx+1, cur*next, plus, minus, multiple-1, divide)
    if divide > 0:
        dfs(idx+1, int(cur/next), plus, minus, multiple, divide-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, multiple, divide = map(int, input().split())
    nums = list(map(int, input().split()))

    maximum = -100000000
    minimum = 100000000
    dfs(1, nums[0], plus, minus, multiple, divide)
    print(f"#{tc} {maximum - minimum}")