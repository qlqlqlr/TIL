import copy
N, M = map(int, input().split())
lst = list(map(int, input().split()))
path = []   # 선택도니 패들의 값을 저장할 리스트
used = [0] * N   # 패가 사용되었는지 체크    bit
mini = 21e9       # 임의의 엄청 큰수
result = []

def DFS(level, sum):
    global mini, path, result
    if level == M:        # 패를 선택 했다면
        print(path)
        if sum < mini:     # 현재 곱의 값이 최소값보다 작을경우
            mini = sum
            result = copy.deepcopy(path)    #선택된 패들의 값을 퇴종 result 에 작성

        return

    for i in range(N):
        if used[i] == 1:
            continue
        path.append(lst[i])   # 패들 성택하고 path에 추가
        used[i] = 1
        DFS(level + 1, sum * lst[i])        # 다음 패들 선택으로 넘어가면서 곱해줌
        used[i] = 0               # 복구 (백트래킹)
        path.pop()

DFS(0, 1)   #초기레벨은 0 초기곱은 1

result.sort()
print(*result)