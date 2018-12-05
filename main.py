import numpy as np
import sys
while True:
    try:
        T=int(sys.stdin.readline())
        N = [i for i in range(T)]
        M = [i for i in range(T)]
        reads=[i for i in range(T)]
        for j in range(0,T):
            NM =sys.stdin.readline()
            N[j] = int(NM.split(' ')[0])
            M[j] = int(NM.split(' ')[1])
            reads[j]=sys.stdin.readline().strip('\n').strip()
        for j in range(0,T):
            a = list(reads[j].split(' '))
            a = map(int, a)
            b = np.zeros(5)
            if M[j] < N[j]:
                for i in range(0, 3):
                    if i == 0:
                        b[i] = a[i + M[j]] - 1
                    elif i == N[j] - M[j]:
                        b[i] = 100 - a[i - 1] - 1
                    else:
                        b[i] = a[i + M[j]] - a[i - 1] - 1
                result = b.max()
            else:
                result = 100

            sys.stdout.write(str(int(result))+'\n')

    except EOFError:
        break
