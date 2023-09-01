# 수학 게임 페스티벌
def double(num):
    return (num * 2) % 10000


def subtract(num):
    return (num - 1) if num != 0 else 9999


def left_rotate(num):
    return (num % 1000) * 10 + (num // 1000)


def right_rotate(num):
    return (num % 10) * 1000 + (num // 10)


def bfs(start, target):
    visited = set()
    queue = [(start, "")]

    while queue:
        current, actions = queue.pop(0)
        if current == target:
            return actions

        for action, func in [('D', double), ('S', subtract), ('L', left_rotate), ('R', right_rotate)]:
            next_num = func(current)
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, actions + action))

    return ""


# 입력 받기
N = int(input())
for _ in range(N):
    initial, target = map(int, input().split())
    result = bfs(initial, target)
    print(result)

