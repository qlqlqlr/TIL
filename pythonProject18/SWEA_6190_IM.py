# 정곤이의 단조 증가하는 수


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    def ch():
        maxi = 0
        for i in range(N):
            for j in range(i + 1, N):
                num = nums[i] * nums[j]
                num = str(num)
                for k in range(1, len(num)):
                    if num[k] < num[k - 1]:
                        break

                else:
                    num = int(num)
                    if num > maxi:
                        maxi = num

        if maxi == 0:
            maxi = -1
        return maxi

    print(f'#{tc} {ch()}')