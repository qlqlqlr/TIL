# swea 문제 솔빙 클럽 최소 시장 트리 (유니온 파인드)




def find_set(x):
   if parents[x] == x:
       return x

   parents[x] = find_set(parents[x])
   return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        # 사이클 발생
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        f, t, w = map(int, input().split())
        edge.append([f, t, w])
    # w 를 기준으로 정렬
    edge.sort(key=lambda x: x[2])

    # 사이클 발생 여부를 union find 로 해결
    parents = [i for i in range(V + 1)]
    cnt = 0
    sum_weight = 0
    for f, t, w in edge:
        # 싸이클이 발생하지 않는다면
        if find_set(f) != find_set(t):
            cnt += 1
            sum_weight += w
            union(f, t)
            # MST 구성이 끝나면
            if cnt == V:
                break
    print(f'#{tc} {sum_weight}')