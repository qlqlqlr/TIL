
def solution():
    def f(num):
        global N, arr, M, query
        L, R = -1, N
        while L + 1 < R :
            mid = (L + R) // 2
            if arr[mid] >= num : R = mid
            else : L = mid
        if (R != N and arr[R] == num) or (N == 1 and arr[0] == num ): return 1
        else : return 0