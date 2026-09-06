def calc(N, idx, answer):
    if N % nums[idx] == 0:
        N = N // nums[idx]
        answer[idx] += 1
        calc(N, idx, answer)
    else:
        return N, answer

T = int(input())
nums = [2, 3, 5, 7, 11]

for test_case in range(1, T+1):
    N = int(input())
    answer = [0, 0, 0, 0, 0]
    for i in range(5):
        calc(N, i, answer)
    print(answer)


