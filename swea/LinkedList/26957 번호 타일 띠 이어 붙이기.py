class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split())) # 첫 번째 띠
    size = N
    head = Node(arr[0])
    current = head
    for a in arr[1:]:
        new_node = Node(a)
        current.next = new_node
        current = new_node

    for _ in range(M-1):
        row = list(map(int, input().split()))
        current = head
        changed = False
        for s in range(size-1):
            if s == 0 and row[0] < current.data:
                new_head = Node(row[0])
                new_head.next = head
                head = new_head
                current = head
                temp_node = current.next
                for r in row[1:]:
                    new_node = Node(r)
                    current.next = new_node
                    new_node.next = temp_node
                    current = new_node
                changed = True
                break
            elif row[0] < current.next.data:
                temp_node = current.next
                for r in row:
                    new_node = Node(r)
                    current.next = new_node
                    new_node.next = temp_node
                    current = new_node
                changed = True
                break
            else:
                current = current.next
        if not changed:
            for r in row:
                new_node = Node(r)
                current.next = new_node
                current = new_node
        size += N

    total_list = []
    current = head
    for _ in range(size):
        total_list.append(current.data)
        current = current.next
    print(f"#{test_case}", *total_list[-1:-11:-1])