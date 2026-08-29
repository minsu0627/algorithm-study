T = int(input())
for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    answer = int(round(sum(nums[1:-1])/len(nums[1:-1]),0))
    print(f"#{test_case} {answer}")