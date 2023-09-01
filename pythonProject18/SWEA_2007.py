# 2007 패턴 마디의길이


T = int(input())
D = 30
for tc in range(1, T + 1):
    arr = input()
    def ch():
        madi = ''
        result = 0
        for i in range(1, 10):
            if arr[0] == arr[i] and arr[1] == arr[i + 1] and arr[2] == arr[i + 2]:
                madi += arr[0:i]
                break
        if madi in arr[i:] and len(madi) != 0:
            result = len(madi)
        else:
            result = 0


        print(f'#{tc} {result}')

    ch()