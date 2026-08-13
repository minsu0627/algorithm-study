for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    for i in range(2, N - 2):
        temp = []
        # 기준이 되는 빌딩의 좌우 2개의 빌딩 높이 검사
        for j in range(-2, 3):
            if j == 0:
                continue
            else:
                diff = buildings[i] - buildings[i - j]
                temp.append(diff)
        cnt = min(temp)
        if cnt <= 0:
            continue
        else:
            answer += cnt
    print(f"#{test_case} {answer}")