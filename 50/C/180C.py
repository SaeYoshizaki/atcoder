def Divisor_list(N):
    divisor = []
    i = 1
    while i**2 <= N:
        if N % i == 0:
            divisor.append(i)
            if i != N // i:
                divisor.append(N // i)  
        i += 1
    divisor.sort()
    return divisor


def main():
    N = int(input())
    result = Divisor_list(N)
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
