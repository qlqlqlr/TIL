# union -> 두 그룹을 하나로 합친다
# find -> 특정 노드가 어느 그룹에 속해있는지 찾는다

def find(node):
    if node != root[node]:
        root[node] = find(root[node])

    return root[node]

def union(x, y):
    root_x = find(x)   # x의 루트 부모 찾기
    root_y = find(y)

    if rank[root_x] > rank[root_y]:   # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
        root[root_y] = root_x

    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:     # 만약 랭크가 같다면 y의 랭크 증가
            rank[root_y] += 1


N, Q = map(int, input().split())
rank = [0] * (N + 1)
root = [i for i in range(N + 1)]

for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B):   # A 와 B 가 같은 그룹에 속하면
            print('YES')
        else:
            print('NO')
    else:
        union(A, B)          # A와 B를 같은 그룹으로 연결