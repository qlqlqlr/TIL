# 슈퍼 마리오

mushroom = [int(input()) for _ in range(10)]
total = 0

for i in range(10):
    total += mushroom[i]
    if total == 100:
        print(100)
        break

    elif total > 100:
        if total - 100 < 100 - (total - mushroom[i]):
            print(total)
            break
        elif total - 100 == 100 - (total - mushroom[i]):
            print(total)
            break
        else:
            print(total - mushroom[i])
            break

else:
    print(total)
