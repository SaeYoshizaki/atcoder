def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    count = 0
    counter = 0
    for i in range(N-1):
        for j in range(M):
            if list(S[i])[j] != list(S[i+1])[j]:
                count += 1
            else:
                continue
            print(count)
        count == 0
        # if count != 1:
        #     print("No")
        #     exit()
        # else:
        #     count = 0
        #     continue



if __name__ == "__main__":
    main()



    """
    i番目と、i+1番目がM-1文字が一致していればOK
    NもMも値が小さいから、無理やり全てに対して探索をしても大丈夫なのでは？？
    """