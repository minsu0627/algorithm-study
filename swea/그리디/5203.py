# 베이비진 게임
import sys
sys.stdin = open('input.txt', 'r')

def check(have, cur):
    global winner
    if have[cur][1] >= 3:
        winner = True
        return winner

    for j in range(8):
        if have[j][1] > 0 and have[j+1][1] > 0 and have[j+2][1] > 0:
            winner = True
            return winner

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player_1 = [[i, 0] for i in range(10)]
    player_2 = [[i, 0] for i in range(10)]
    winner = False
    for i in range(12):
        if i % 2 == 0:
            player_1[cards[i]][1] += 1
            if check(player_1, cards[i]):
                print(f"#{tc} 1")
                break
        else:
            player_2[cards[i]][1] += 1
            if check(player_2, cards[i]):
                print(f"#{tc} 2")
                break

    if not winner:
        print(f"#{tc} 0")