def main():
    chars = list(input().strip())
    i = int(chars[0])
    j = int(chars[2])
    if j<8:
        print(i, "-", j+1, sep='')
    elif i < 8 and j == 8:
        print(i+1, "-", 1, sep='')
    elif i==8 and j == 8:
        print(8, "-", 8, sep='')
    
if __name__ == "__main__":
    main()