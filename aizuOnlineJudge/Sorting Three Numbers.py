def main():
    inputArr = list(map(int, input().split()))
    A = min(inputArr)
    inputArr.remove(A)
    B = min(inputArr)
    inputArr.remove(B)
    C = min(inputArr)

    print(A, B, C)


if __name__ == "__main__":
    main()


"""
sortで良い。
inputArr.sort()
print(*inputArr)
でOK

ちなみに、
sortは、元のリスト自身を並び替える。
sortedはソートをした新たなリストを作成する。

"""
