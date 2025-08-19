def main():
    N = list(map(int, input()))
    if (sum(N) % 3) == 0:
        print(0)
    print(N)


if __name__ == "__main__":
    main()