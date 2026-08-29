# [초기 아이디어]
# 1.오렌지와 블루의 게이지를 따로 만들기
# 2.버튼 수 N만큼 순회하기
# 3.순서인 로봇(a)이 버튼 누르는 동안 다른 로봇(b)은 게이지 채우기
# 4.로봇(b)의 차례가 왔을 때 가야하는 칸과 현재 칸의 차이 구해서 모은 게이지와 비교
# 5.모은 양이 더 많다면 바로 버튼 누르고 아니라면 모은 만큼 이동 후 버튼까지 이동해서 누르기
# 예상 시간복잡도 : 순회하는 N만큼 -> O(N)
def move(color, num, answer, gauge):
    opponent_gauge = 0 # 해당 컬러가 이동하는 동안 다른 컬러의 게이지
    if color < num: # 해당 컬러가 가야하는 칸보다 작은지 확인
        if color + gauge >= num: # 게이지를 더해서 가야하는 칸보다 크다면
            color = num # 그 칸으로 이동
        else: # 해당 컬러가 가야하는 칸보다 작다면
            color += gauge # 다른 칸이 버튼을 누르는 동안 이동한 만큼 더 하고 추가 이동
            while color != num:
                color += 1
                answer += 1
                opponent_gauge += 1 # 해당 컬러가 이동하는 동안 다른 컬러의 게이지 모음
    else: # 반대의 상황으로 해당 컬러가 음의 방향으로 이동해야하는 경우
        if color - gauge <= num: # 가야하는 칸보다 더 음수쪽으로 갔다면 버튼이 있는 칸으로 이동
            color = num
        else:
            color -= gauge # 해당 컬러가 가야하는 칸보다 크다면 다른 컬러가 버튼 누르는 동안 이동한 만큼
            while color != num: # 음의 방향으로 이동 후 추가 이동
                color -= 1
                answer += 1
                opponent_gauge += 1
    answer += 1 # 해당 컬러가 버튼에 도착하고 버튼을 누르는 시간
    opponent_gauge += 1
    return color, answer, opponent_gauge


T = int(input())
for test_case in range(1, T+1):
    temp = input().split()
    N = int(temp[0])
    buttons = temp[1:]

    orange = 1
    blue = 1
    answer = 0
    orange_gauge = 0
    blue_gauge = 0

    for i in range(0, len(buttons), 2):
        robot, num = buttons[i], int(buttons[i+1])
        if robot == 'O':
            orange, answer, opponent_gauge = move(orange, num, answer, orange_gauge)
            orange_gauge = 0 # 소모한 게이지 초기화
            blue_gauge += opponent_gauge
        else:
            blue, answer, opponent_gauge = move(blue, num, answer, blue_gauge)
            blue_gauge = 0
            orange_gauge += opponent_gauge
    print(f"#{test_case} {answer}")