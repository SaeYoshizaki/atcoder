import sys

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    total = sum(min(a, b) for a, b in zip(A, B))

    out_lines = []
    for _ in range(Q):
        C, X, V = input().split()
        X = int(X)
        V = int(V)
        i = X - 1

        beforesum = min(A[i], B[i])
        if C == 'A':
            A[i] = V
        else:
            B[i] = V
        aftersum = min(A[i], B[i])

        total += aftersum - beforesum
        print(total)

if __name__ == "__main__":
    main()