T = int(input())
for test_case in range(1, T+1):
    board, change = input().split()
    change = int(change)

    candidates = set([board])
    for _ in range(change):
        temp = set()
        for c in candidates:
            num = list(c)

            for i in range(len(num)-1):
                for j in range(i+1, len(num)):
                    num[i], num[j] = num[j], num[i]
                    temp.add(''.join(num))
                    num[i], num[j] = num[j], num[i]
        candidates = temp
    print(f"#{test_case} {max(candidates)}")

# 최대 자릿수는 6이므로 최대 6! = 720 이기 때문에 전체 탐색
# 단, 중복 제거를 위한 set 사용
# 기존 candidates에 저장돼있는 이전 변경들은 필요없기 때문에
# 각 change 순서마다 저장해놓은 temp로 바로바로 덮어쓰기
# set에 처음에 string 타입인 board를 넣으면 예제와 같은 32888의 경우 -> 3, 2, 8이 되기 때문에
# 처음에는 리스트로 감싸서 넣어주고 그 다음 temp에 저장할 때는 add를 통해서 저장
# (add는 데이터 분해하지 않고 통째로 넣음)