# 회의실 배정



n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key = lambda x : (x[1], x[0]))  #회의가 끝나는 시간 기준으로 정렬, 끝나는 시간 같으면 시작시간 순으로 정렬
cnt = 1
time = meetings[0][1]  # 첫 회의가 끝나는 시간
for i in range(1, n):
    if meetings[i][0] >= time:
        cnt += 1   #1. 회의 진행
        time = meetings[i][1]  #2. 끝나는 시간 갱신

print(cnt)