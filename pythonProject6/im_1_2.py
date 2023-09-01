# IM형 기출 강사님 풀이
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcode = list(map(int, input().split()))
#
#     cnt = 0
#     result = 0
#
#     for i in range(N):
#         if passcode[cnt] == sample[i]:
#             cnt += 1
#         if cnt == K:
#             result = 1
#             break
#
#     print(f'#{tc} {result}')



## 두번쨰 풀이


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    indexes = []
    result = 1

    for i in range(len(passcode)):
        now = passcode[i]
        try:
            index = sample.index(now)
            sample = sample[index + 1 :]
        except:
            result = 0

    print(f'#{tc} {result}')