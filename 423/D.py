def main():
    N, K = map(int, input().split())
    machi_time = []
    machi_people = []
    nokori = K
    time = 0
    for _ in range(N):
        A, B, C = map(int, input().split())
        if nokori <= C:
            time = A
            print(time)
            machi_people.append(C)
            machi_time.append(B+A)
            
        else:
            while not (machi_people[idx] + nokori <= C):
                m = min(machi_time)
                idx = machi_time.index(m)
            time += m
            print(time)

if __name__ == "__main__":
    main()