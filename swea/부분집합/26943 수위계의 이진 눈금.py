T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    output = ''

    while len(output) <= 12:
        N *= 2
        if N == 1:
            output += '1'
            break
        elif N > 1:
            N -= 1
            output += '1'
        else:
            output += '0'

    if len(output) <= 12:
        print(f"#{test_case} {int(output)}")
    else:
        print(f"#{test_case} overflow")
