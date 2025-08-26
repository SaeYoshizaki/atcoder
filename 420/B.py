def main():
    arr = []
    people, number = map(int, input().split())
    for _ in range(people):
        s = input().strip()
        s = s.zfill(number)[:number]
        arr.append([int(ch) for ch in s])
    AnsArr = [0] * people


    for i in range(number):
        x = 0
        y = 0
        for j in range(people):
            if arr[j][i] == 0:
                x += 1
            else:
                y += 1
        
        if x < y:
            for j in range(people):
                if arr[j][i] == 0:
                    AnsArr[j] += 1
        else: 
            for j in range(people):
                if arr[j][i] == 1:
                    AnsArr[j] += 1
    max_value = max(AnsArr)
    ans = [i + 1 for i, v in enumerate(AnsArr) if v == max_value]
    print(*ans)

if __name__ == "__main__":
    main()