from collections import deque
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    nums = input()
    queue = deque()
    for n in nums:
        queue.append(n)
    candidates = set()
    for _ in range(N // 4):
        for i in range(0, N, N // 4):
            candidates.add(''.join(list(queue)[i:i+(N//4)]))
        temp = queue.pop()
        queue.appendleft(temp)
    candidates = sorted(list(candidates), reverse=True)
    print(f"#{test_case} {int(candidates[K-1], 16)}")
