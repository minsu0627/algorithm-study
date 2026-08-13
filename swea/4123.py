# from itertools import permutations
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     plus, minus, multiple, divide = map(int, input().split())
#     operators = list(set(permutations(['+'] * plus + ['-'] * minus + ['*'] * multiple + ['/'] * divide)))
#     nums = list(map(int, input().split()))
#     maximum = -float('inf')
#     minimum = float('inf')
#
#     for o in range(len(operators)):
#         temp = 0
#         for i in range(N):
#             if i == 0:
#                 temp += nums[i]
#             else:
#                 if operators[o][i-1] == '+':
#                     temp += nums[i]
#                 elif operators[o][i-1] == '-':
#                     temp -= nums[i]
#                 elif operators[o][i-1] == '*':
#                     temp *= nums[i]
#                 else:
#                     temp = int(temp / nums[i])
#         maximum = max(maximum, temp)
#         minimum = min(minimum, temp)
#     print(maximum, minimum)



# max, min 설정
# 오퍼레이터 랜덤 추출(-> 순열 추출)
# 값 계산해서 max, min 업데이트
def dfs(cur, i, plus, minus, multiple, divide):
    if plus == 0 and minus == 0 and multiple == 0 and divide == 0:
        result[0] = max(result[0], cur)
        result[1] = min(result[1], cur)
        return

    if plus > 0:
        dfs(cur + nums[i], i+1, plus-1, minus, multiple, divide)
    if minus > 0:
        dfs(cur - nums[i], i+1, plus, minus-1, multiple, divide)
    if multiple > 0:
        dfs(cur * nums[i], i+1, plus, minus, multiple-1, divide)
    if divide > 0:
        dfs(int(cur / nums[i]), i+1, plus, minus, multiple, divide-1)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    plus, minus, multiple, divide = map(int, input().split())
    nums = list(map(int, input().split()))
    result = [-float('inf'), float('inf')]
    dfs(nums[0], 1, plus, minus, multiple, divide)
    print(f"#{test_case} {result[0] - result[1]}")
