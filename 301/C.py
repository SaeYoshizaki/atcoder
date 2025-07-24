

"""
自分に含まれておらず(いて)、相手に含まれている(いない)ものが全てatcoderの中で置き換えられればOK

1. それぞれの文字に対して、何が何個含まれているのかを辞書で整理
2. 比較
    その値のものが相手に幾つあるのかを比較？
    SをベースにTを探索していく。
    アルファベット順に並んでいるはずだから、一致するものが出てくるまで繰り返す？？
    見つかり次第最初に戻る
    計算量がやばそう

3. 違う文字の数分＠が含まれていない場合 -> No確定&終了
4. 足りないもの同士がatcoderの文字で表せるものなのかを判定
5. できる -> Yes, できない -> No

"""

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
    # Sdict_sorted = func(sorted(Sdict.items(), key=lambda x:x[0]))
    # Tdict_sorted = func(sorted(Tdict.items(), key=lambda x:x[0]))

    atcoder = list("atcoder")

    # まとめた
    Scope = set(Sdict.keys()) | set(Tdict.keys()) 
    if "@" in Scope:
        Scope.remove("@")
    # print(Scope)

    for i in Scope:
        if Sdict[i] == Tdict[i]:
            continue
        elif Sdict[i] > Tdict[i]:
            if i in atcoder:
                Tdict["@"] = Tdict.get("@", 0) - Sdict.get(i, 0) - Tdict.get(i, 0)
            else:
                print("No")
                return
        else:
            if i in atcoder:
                Sdict["@"] = Sdict.get("@", 0) - Tdict.get(i, 0) - Sdict.get(i, 0)
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
"""