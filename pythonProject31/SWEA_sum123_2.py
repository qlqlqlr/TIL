N = int(input())
cnt = 0

def fune(num):
    global cnt
    if num == N: # N 에 도달했다면 하나의 경우의 수를 더 찾았다
        cnt += 1
        return

    if num > N: # num이 N을 넘어가면 가망이 없다.  # 백트래킹
        return

    # 재귀 구성 : 1, 2, 3을 더해서 다음 조합으로 넘어가기
    for i in range(1, 4):
        fune(num + 1)

fune(0)
print(cnt)