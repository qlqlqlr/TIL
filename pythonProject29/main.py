
string = input()
N = len(string)


def ch():
    stack = []

    start = 0
    i = 1
    while True:
        if not string[i].isdigit():
            stack.append(string[start:i])
            stack.append(string[i])

            start = i + 1


        if i == N - 1:
            stack.append(string[start:i+1])
            break


        i += 1


    M = len(giho)
    for j in range(M - 1):
        if giho[j] == '-' and giho[j + 1] == '+':



ch()