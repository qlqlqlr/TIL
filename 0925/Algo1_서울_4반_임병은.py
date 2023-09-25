
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = input()
    key = input()
    result = []
    imp = 0

    if key == 'A':
        key = 0xa
    elif key == 'B':
        key = 0xb
    elif key == 'C':
        key = 0xc
    elif key == 'D':
        key = 0xd
    elif key == 'E':
        key = 0xe
    elif key == 'F':
        key = 0xf
    elif key == '1':
        key = 0x1
    elif key == '2':
        key = 0x2
    elif key == '3':
        key = 0x3
    elif key == '4':
        key = 0x4
    elif key == '5':
        key = 0x5
    elif key == '6':
        key = 0x6
    elif key == '7':
        key = 0x7
    elif key == '8':
        key = 0x8
    elif key == '9':
        key = 0x9
    elif key == 'F0':
        key = 0x0

    for i in range(N):
        if P[i] == '1':
            imp = 0x1
        elif P[i] == '0':
            imp = 0x0
        elif P[i] == '2':
            imp = 0x2
        elif P[i] == '3':
            imp = 0x3
        elif P[i] == '4':
            imp = 0x4
        elif P[i] == '5':
            imp = 0x5
        elif P[i] == '6':
            imp = 0x6
        elif P[i] == '7':
            imp = 0x7
        elif P[i] == '8':
            imp = 0x8
        elif P[i] == '9':
            imp = 0x9
        elif P[i] == 'A':
            imp = 0xa
        elif P[i] == 'B':
            imp = 0xb
        elif P[i] == 'C':
            imp = 0xc
        elif P[i] == 'D':
            imp = 0xd
        elif P[i] == 'E':
            imp = 0xe
        elif P[i] == 'F':
            imp = 0xf

        result.append(imp ^ key)

    print(f'#{tc}', end=' ')
    H = ''
    for i in range(len(result)):
        ans = hex(result[i])
        H += str.capitalize(ans[2:])
    print(H)


