from decimal import Decimal, getcontext

def main():
    getcontext().prec = 20
    S = list(input())
    N = len(S)
    ans = []
    count = 0
    for i in range(N):
        if S[i] == 't':
            count += 1
            ans.append(i)
    if not ans or (len(ans) < 3):
        print("0.00000000000000000")
        exit()
    ansN = len(ans)
    B = 0
    for j in range(ansN):
        for i in range[ansN - i]
        lenN = ans[i] - ans[j]
            print(abs(A))
            if A == 2:
                continue
            answer = (Decimal(count) - Decimal(2)) / (Decimal(A) - Decimal(2))
            print(answer)
        if answer > B:
            B = answer
            print(B)
    # print(B)
    # print(f"{answer:.17f}")



if __name__ == "__main__":
    main()