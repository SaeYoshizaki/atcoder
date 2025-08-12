def main():
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        AnsArr = []
        count = 0
        for j in range(H):
            for i in range(W):
                if (j + i) % 2 == 0:
                    AnsArr.append("#")
                else:
                    AnsArr.append(".")
            print("".join(AnsArr))
            AnsArr = []
        print()

if __name__ == "__main__":
    main()