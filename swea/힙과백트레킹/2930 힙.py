# 힙
import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    max_heap = []
    answer = []
    for _ in range(N):
        op = list(map(int, input().split()))
        if op[0] == 1:
            heapq.heappush(max_heap, -op[1])
        else:
            if max_heap:
                answer.append(-heapq.heappop(max_heap))
            else:
                answer.append(-1)

    print(f"#{tc}", *answer)

