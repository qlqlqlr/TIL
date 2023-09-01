
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()
    can = []     # 당근의 포장조건을 만족하는 개수 차이
    for i in range(1, N - 1):          # 첫번쨰 상자와 두번쨰 상자 사이
        for j in range(i + 1, N):     # 두 번째 상자와 세번째 상자 사이
            A = Ci[:i]      # 첫번째 상자
            B = Ci[i:j]
            C = Ci[j:]
            if A[-1] == B[0] or B[-1] == C[0]:  # 같은 크기의 당근이 인접한 상자에 있으면
                continue
            if len(A) * len(B) * len(C) == 0:   # 빈 상자가 있으면
                continue
            if len(A) > N // 2 or len(B) > N // 2 or len(C) > N // 2: # 한 상자에 N // 2 를 초과하는 당근이 있으면
                continue
            can.append(max(abs(len(A) - len(B)), abs(len(B) - len(C)), abs(len(C) - len(A))))
    try:
        print(f'#{tc} {min(can)}')
    except:
        print(f'#{tc} -1')