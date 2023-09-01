# 강사님 풀이

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        arr.append(arr.pop(0))         # 맨앞에꺼 뽑아서 맨뒤에 넣어준다

    result = arr[0]
    print(f'#{tc} {result}')
