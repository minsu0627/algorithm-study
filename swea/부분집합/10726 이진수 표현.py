def check(arr):
    if len(arr) < N:
        return 'OFF'

    if len(arr) > N:
        arr = arr[-N:]

    for a in arr:
        if a == '0':
            return 'OFF'
    return 'ON'

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    transformed = format(M, 'b')
    print(f"#{test_case} {check(transformed)}")