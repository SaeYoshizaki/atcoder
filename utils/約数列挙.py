def Divisor_list(N):
    divisor = []
    i = 1
    while i**2 < N:
        if N % i == 0:
            divisor.append(i)
        if i != N // i:
            divisor.append(N // i)
        i += 1
        divisor.sort()
    return divisor
