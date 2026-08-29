import heapq

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    answer = []
    max_heap = []
    for _ in range(N):
        op = list(map(int, input().split()))
        if len(op) == 2:
            heapq.heappush(max_heap, -op[1])
        else:
            if max_heap:
                answer.append(-heapq.heappop(max_heap))
            else:
                answer.append(-1)
    print(f"#{test_case}", *answer)