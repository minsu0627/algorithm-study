T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    N_nums = {num:1 for num in (list(map(int, input().split())))}
    K = int(input())
    K_nums = list(map(int, input().split()))

    for num in K_nums:
        N_nums[num] = 0
    
    answer = []
    for k, v in N_nums.items():
        if v == 1:
            answer.append(k)
    print(f"#{test_case}", *answer)