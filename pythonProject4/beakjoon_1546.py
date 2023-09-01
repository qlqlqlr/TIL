# 평균

N = int(input())
score = list(map(int, input().split()))
new_score = []

high = max(score)
score.remove(high)
new_score.append(100)



for i in range(len(score)):
    new = score[i] / high * 100
    new_score.append(new)

print((sum(new_score) / len(new_score)))