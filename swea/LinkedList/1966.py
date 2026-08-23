T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f"#{test_case}", *sorted(list(map(int, input().split()))))