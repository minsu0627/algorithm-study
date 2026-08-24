# 일반 insert 사용
# T = int(input())
# for test_case in range(1, T+1):
#     N, M, L= map(int, input().split())
#     songs = list(map(int, input().split()))
#     for _ in range(M):
#         p, v = map(int, input().split())
#         songs.insert(p, v)
#     print(f"#{test_case} {songs[L]}")

# Linked List 사용
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    songs = list(map(int, input().split()))

    head = Node(songs[0])
    current = head

    for i in range(1, N):
        new_node = Node(songs[i])
        current.next = new_node
        current = new_node

    for j in range(M):
        p, v = map(int, input().split())
        current = head

        for _ in range(p-1):
            current = current.next

        temp_node = current.next
        add_node = Node(v)
        current.next = add_node
        add_node.next = temp_node

    current = head
    for k in range(L):
        current = current.next
    print(f"#{test_case} {current.data}")
