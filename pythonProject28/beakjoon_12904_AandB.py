
# A와 B

S = list(input())
T = list(input())


def ch(S, T):

    while len(S) != len(T):
        n = len(T)
        if T[n-1] == 'A':
            T = T[:n - 1]

        elif T[n-1] == 'B':
            T = T[:n - 1]
            for i in range(len(T)):
                if T[i] == 'A':
                    T[i] = 'B'
                else:
                    T[i] = 'A'

        if len(S) == len(T):
            if S != T:
                print(0)
                exit()
    print(1)

ch(S, T)