import heapq

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
    
    node = len(nums) - 1
    answer = 0
    while node > 0:
        node = (node - 1) // 2
        answer += heap[node]
    print(f"#{test_case} {answer}")

