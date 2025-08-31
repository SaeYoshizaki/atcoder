import numpy as np
def main():
    N = int(input())
    inputS = input()
    S = list(inputS)
    S0 = S[0]
    odd_list = [x for x in range(N*2) if x % 2 != 0]
    even_list = [x for x in range(N*2) if x % 2 == 0]
    ansArr = ([i for i, x in enumerate(S) if x == S0])
    count = 0

    even = np.array(even_list)-np.array(ansArr)
    even_sum = sum(np.abs(even))
    odd = np.array(odd_list)-np.array(ansArr)
    odd_sum = sum(np.abs(odd))
    if (even_sum < odd_sum):
        print(even_sum)
    else:
        print(odd_sum)

if __name__ == "__main__":
    main()