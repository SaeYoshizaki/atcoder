def main():
    A = int(input())
    N = int(input())
    palaindArr = palaind_number(N)
    print(base_n(palaindArr, A))
    palaind_arr(base_n(palaindArr, A))
    base_8_to_10(palaind_arr(base_n(palaindArr, A)))
    print(sum(base_8_to_10(palaind_arr(base_n(palaindArr, A)))))
    

    

def palaind_number(inputNumber):
    palind_base_10 = []
    for i in range(inputNumber):
        if palindrome(i+1):
            palind_base_10.append(i+1)
    print(palind_base_10)
    return palind_base_10

def base_n(inputArr, N):
    length = len(inputArr)
    result_Nshinhou =[]
    
    for i in range(length):
        Nshinhou: list[int] = []
        x = inputArr[i]
        while x > 0:
            Nshinhou.append(x % N)
            x = x // N

        Nshinhou = list(reversed(Nshinhou))
        result_Nshinhou.append(int("".join(map(str, Nshinhou))))
    return result_Nshinhou

def base_8_to_10(inputArr):
    length = len(inputArr)
    result_Nshinhou = []
    
    for i in range(length):
        x = inputArr[i]
        result_Nshinhou.append(int(str(x), 8))
        
    return result_Nshinhou


def palaind_arr(inputArr):
    palind_base_n = []
    length = len(inputArr)
    for i in range(length):
        if palindrome(inputArr[i]):
            palind_base_n.append(inputArr[i])
    print(palind_base_n)
    return palind_base_n





def palindrome(number):
    return str(number) == str(number)[::-1]


if __name__ == "__main__":
    main()