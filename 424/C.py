from collections import deque
def main():

    N = int(input())
    G = [[] for _ in range(N+1)] 
    start = []
    for i in range(1, N+1):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            start.append(i)
        else:
            G[a].append(i)
            G[b].append(i)
    ans = 0

    used = [False]*(N+1)
    q = deque(start)

    while len(q) > 0:
        v = q.popleft()
        if not used[v]:
            used[v] = True
            ans += 1
            for w in G[v]:
                if not used[w]:
                    q.append(w)
    print(ans)

if __name__ == "__main__":
    main()