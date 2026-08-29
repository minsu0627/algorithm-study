T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    boxes = sorted(list(map(int, input().split())), reverse=True)
    workers = sorted(list(map(int, input().split())), reverse=True)
    answer = 0

    for b in boxes:
        if workers and workers[0] >= b:
            answer += b
            workers.pop(0)
    print(f"#{test_case} {answer}")