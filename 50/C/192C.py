def descending_order(N):
    NArr = [int(x) for x in list(str(N))]
    ordered_NArr = sorted(NArr, reverse=True)
    str_list = map(str, ordered_NArr)
    list_join = int(''.join(str_list))
    return list_join

def increasing_order(N):
    NArr = [int(x) for x in list(str(N))]
    ordered_NArr = sorted(NArr)
    str_list = map(str, ordered_NArr)
    list_join = int(''.join(str_list))
    return list_join

def main():
    N, K = map(int, input().split())
    # print(descending_order(N))
    # print(increasing_order(N))
    for _ in range(K):
        N = descending_order(N) - increasing_order(N)
    print(N)

if __name__ == "__main__":
    main()