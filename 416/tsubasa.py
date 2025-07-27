def main():
    S = input()
    T = ""
    sharp_count = 0
    total_sharp_count = 0
    o_count = 0
    
    for i in S:
        if i == "#":
            T += "#"
            sharp_count += 1
            total_sharp_count += 1
        elif sharp_count > 0:
            T += "o"
            o_count += 1
            sharp_count = 0
        else:
            T += "."
            
    new_T = ""
    if total_sharp_count == 0:
        for i in range(len(T)-1):
            new_T += "."
        new_T += "o"
        T = new_T
    
    current = ""
    if total_sharp_count != o_count and total_sharp_count != 0:
        for i in range(len(T)):
            if current == "o" and T[i] == "o":
                new_T += "."
                current = "."
            elif T[i] == "." and total_sharp_count != o_count and current != "o":
                new_T += "o"
                o_count += 1
                current = "o"
            else:
                new_T += T[i]
                current = ""
        T = new_T
    print(T)
    
if __name__ == "__main__":
    main()
