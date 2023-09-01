
# 컨테이너 운반

T = int(input())
for tc in range(1, T +1):
    N, M = map(int, input().split())

    con = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    con.sort(reverse=True)
    truck.sort(reverse=True)
    cnt = 0
    j = 0
    for i in range(M):
        if i < N:
            while j < N:
                if truck[i] >= con[j]:
                    cnt += con[j]
                    j += 1
                    break
                else:
                    j += 1






        else:
            break

    print(f'#{tc} {cnt}')