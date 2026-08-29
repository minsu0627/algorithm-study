T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = input().split()
    mid = (N+1) // 2
    #먼저 나눈 카드
    cards_a = cards[:mid]
    #두 번째로 나눈 카드
    cards_b = cards[mid:]
    answer = []
    for i in range(len(cards_b)):
        answer.append(cards_a[i])
        answer.append(cards_b[i])
    if len(cards_a) > len(cards_b):
        answer.append(cards_a[-1])
    print(f"#{test_case} {' '.join(answer)}")