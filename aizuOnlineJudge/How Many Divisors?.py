def main():
    a, b, c = map(int, input().split())
    divisor = list(i for i in range(1, c + 1) if c % i == 0)
    count = 0
    for i in range(a, b + 1):
        for j in range(len(divisor)):
            if i == divisor[j]:
                count += 1

    print(count)


if __name__ == "__main__":
    main()


# こんなことしなくてもこれで良い
"""def main():
    count = 0
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if c % i == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
"""
