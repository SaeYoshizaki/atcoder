def main():
    X, K, D = map(int, input().split())
    # X: 現在地
    # K: 移動回数
    # D: 移動距離
    X = abs(X)
    border = X // D
    if border >= K:
        print(X-K*D)
        exit()
    else:
        if X-border*D <= abs(X-(border+1)*D):
            tmp_min = X-border*D
        else:
            tmp_min = X-(border+1)*D
            border += 1
    left = (K-border) % 2
    if left == 1:
        if abs(tmp_min + D) <= abs(tmp_min - D):
            print(tmp_min + D)
        else:
            print(abs(tmp_min - D))
    else:
        print(tmp_min)
        
        
        

    

if __name__ == "__main__":
    main()