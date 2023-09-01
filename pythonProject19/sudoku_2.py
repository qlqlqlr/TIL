# SWEA 1974. 스도쿠 검증

def check(arr):
    for i in range(9):
        row = [0] * 10   # 가로줄 검사 리스트
        col = [0] * 10   # 세로줄
        for j in range(9):
            # 가로줄에 숫자가 등장한 것에 대한 count
            row[arr[i][j]] += 1
            # 숫자가 두번 이상 등장했다 -> return 0
            if row[arr[i][j]] >= 2:
                return 0
            col[arr[j][i]] += 1
            if col[arr[j][i]] >= 2:
                return 0
        # 3x3 작은 격자 검사
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                matrix = [0] * 10
                # 격자의 각 요소 검사
                for i in range(3):
                    for j in range(3):
                        matrix[arr[y + i][x + j]] += 1
                        if matrix[arr[y + i][x + j]] >= 2:
                            return 0
        #모든 검사를 통과하면 유효하므로 return 1
        return 1