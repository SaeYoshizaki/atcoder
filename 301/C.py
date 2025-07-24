from collections import Counter



def func(samples):
    list1 = []
    list2 = []
    for a, b in samples:
        list1.append(a)
        list2.append(b)
    return list1, list2

def main():
    S = list(input())
    T = list(input())

    # 1. それぞれの文字に対して、何が何個含まれているのかを辞書で整理

    Sdict = Counter(S)
    Tdict = Counter(T)

    atcoder = list("atcoder")

    # まとめた
    Scope = set(Sdict.keys()) | set(Tdict.keys()) 
    if "@" in Scope:
        Scope.remove("@")

    for i in Scope:
        if Sdict[i] == Tdict[i]:
            continue
        elif Sdict[i] > Tdict[i]:
            if i in atcoder and "@" in Tdict.keys() and Tdict["@"] >= (Sdict[i] - Tdict[i]):
                Tdict["@"] -= (Sdict[i] - Tdict[i])
            else:
                print("No")
                return
        else:
            if i in atcoder and "@" in Sdict.keys() and Sdict["@"] >= (Tdict[i] - Sdict[i]):
                Sdict["@"] -= (Tdict[i] - Sdict[i])
            else:
                print("No")
                return
    if Tdict["@"] == Sdict["@"]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()






"""
memo
S: ch@ku@ai
T: choku@@i

やっぱり少ない方の＠の数をひくのが一番？？
＠は一番最後に大きさが一致すれば十分である。
S-T 
atcoder
atcodert
at@@@@@@
"""