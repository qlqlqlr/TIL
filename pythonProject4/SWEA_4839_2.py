# SWEA 4839. 이진탐색

def binary_search(pages, p):
    start = 1
    end = pages
    mid = 0
    cnt = 1
    # 만약 middle이 p와 같다면, 찾는 값 p를 찾은것이므로 탐색을 종료
    while p != mid:
        mid = int((start + end) // 2)
        if mid > p:
            end = mid
        else:
            start = mid
        cnt += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    P, pa, pb = map(int, input().split())
    A = binary_search(P, pa)
    B = binary_search(P, pb)
    result = 0
    if A == B:
        result = 0
    elif A < B:
        result = 'A'
    else:
        result = 'B'

    print(f'#{tc} {result}')