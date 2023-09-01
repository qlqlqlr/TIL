# 오후 DFS 실습
# 8개의 알파벳으로 구성 도니 문자열과 대응되는 인접행렬을 입력받아주세요
# 아래 이미지는 입력 예시에 해당하는 트리입니다.
# 0 번 알파벳부터 DFS로 노드들을 탐색하면서 출력해 주세요.


def Dfs(n, V, adj_m, Alp):
    stack = []
    visited = [0] * (V)
    visited[n] = 1
    print(Alp[n], end = '')
    while True:
        for w in range(1, V):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                print(Alp[n], end = '')
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    return



Alp = input()
V = len(Alp)
adj_m = [list(map(int, input().split())) for _ in range(V)]

Dfs(0, V, adj_m, Alp)

