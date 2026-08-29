def update_tree(node):
    if node > N:
        return 0
    
    if tree[node] != 0:
        return tree[node]

    tree[node] = update_tree(node * 2) + update_tree(node * 2 + 1)
    return tree[node]

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num
    update_tree(1)
    print(f"#{test_case} {tree[L]}")
