def main():
    N, K = map(int, input().split())
    result = N + K
    if (result <= 12):
        print(result)
    else:
        print(result - 12)

if __name__ == "__main__":
    main()