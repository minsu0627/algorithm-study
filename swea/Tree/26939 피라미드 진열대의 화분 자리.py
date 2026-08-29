def update_tree(node):
    if node > N:
        return

    update_tree(node * 2)
    tree[node] = pot_num[0]
    pot_num[0] += 1
    update_tree(node * 2 + 1)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    pot_num = [1]
    update_tree(1)
    print(f"#{test_case} {tree[1]} {tree[int(N/2)]}")