def main():
    X, C = map(int, input().split())
    ans = (X // (1000 + C)) * 1000
    print(ans)

if __name__ == "__main__":
    main()