tree = [[-1, -1] for _ in range(1001)]

N = 0

preorder = []
inorder = []
postorder = []

def dfs(now):
    # now가 -1이면 장식이 없는경우 return
    if now == -1:
        return
    # 전위순회( 루트 > 왼쪽 > 오른쪽)
    preorder.append(now)
    # 왼쪽으로 탐색
    dfs(tree[now][0])

    # 중위순회(왼쪽 > 루트 > 오른쪽)
    inorder.append(now)
    # 오른쪽으로 탐색
    dfs(tree[now][1])

    # 후위순회 (왼쪽 > 오른쪽 > 루트)
    postorder.append(now)

N = int(input())
for _ in range(N): # 장식의 정보를 입력받기
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right

dfs(1)
print(' '.join(map(str, inorder)))
print(' '.join(map(str, preorder)))
print(' '.join(map(str, postorder)))