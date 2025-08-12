def main():
    A, B = map(int, input().split())
    if A < B:
        print("a < b")
    elif A > B:
        print("a > b")
    else:
        print("a == b")


if __name__ == "__main__":
    main()

    """
    ないとは言えないから、一致している時もelifにしてその他の時をelseにした方が🙆
    """
