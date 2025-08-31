def main():
    count = set()
    N = int(input())
    for i in range(2, 33): # b
        for j in range(2, 100001): # a
            if j**i <= N:
                count.add(j**i)
    print(N-len(count))

if __name__ == "__main__":
    main()