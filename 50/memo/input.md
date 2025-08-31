# Python の入力まとめ

競プロや AtCoder でよく使う Python の `input()` の書き方を整理しました。

---

## 1. 整数を 1 つ読み込む
```python
N = int(input())
```
- 標準入力から 1 行読み込んで、整数に変換する。
```
例: 入力
123
```
```python
出力 → N = 123
```

---

## 2. 数字を 1 桁ずつリストに読み込む
```python
N = list(map(int, input()))
```
- 文字列として入力された数値を 1 文字ずつ整数に変換してリスト化。
```
例: 入力
12345
```
```python
出力 → N = [1, 2, 3, 4, 5]
```

---

## 3. すでに整数として読み込んだものを 1 桁ずつリストに変換
```python
NArr = [int(x) for x in list(str(N))]
```
- `N` が整数の場合に、その桁をリスト化。
```
例: 入力
2025
```
```python
N = 2025
出力 → NArr = [2, 0, 2, 5]
```

---

## 4. 複数の整数を読み込む
```python
N, K = map(int, input().split())
```
- 1 行に複数の整数がスペース区切りで入力される場合に便利。
```
例: 入力
5 7
```
```python
出力 → N = 5, K = 7
```

---

# 他にも覚えておくと便利な入力パターン

## 複数行入力（固定行数）
```python
A = [int(input()) for _ in range(N)]
```
- `N` 行分の整数を 1 つずつ読み込んでリスト化。
```
例: 入力（N=3 の場合）
4
7
9
```
```python
出力 → A = [4, 7, 9]
```

---

## 複数行入力（行ごとに複数の値）
```python
arr = [list(map(int, input().split())) for _ in range(N)]
```
- `N` 行分を読み込み、それぞれ整数のリストにする。
```
例: 入力（N=2 の場合）
1 2 3
4 5 6
```
```python
出力 → arr = [[1, 2, 3], [4, 5, 6]]
```

---

## 文字列をそのまま読み込む
```python
S = input().strip()
```
- 改行を削除した文字列を受け取る。
```
例: 入力
hello world
```
```python
出力 → S = 'hello world'
```

---

## 複数の文字を 1 文字ずつリスト化
```python
chars = list(input().strip())
```
```
例: 入力
abcde
```
```python
出力 → chars = ["a", "b", "c", "d", "e"]
```

---

## 複数行の文字列入力（行ごとにリスト化）
```python
lines = [input().strip() for _ in range(N)]
```
```
例: 入力（N=3 の場合）
abc
def
ghi
```
```python
出力 → lines = ['abc', 'def', 'ghi']
```

---

## 大量入力を高速に読む
```python
import sys
input = sys.stdin.readline
```
- 多量の入力がある場合、`input()` より速く処理できる。
- 末尾に改行が含まれるので `.strip()` を組み合わせるのが基本。
```
例: 入力
42
```
```python
出力 → input() で '42\n' を受け取る（.strip() で '42'）
```

---

# まとめ
- **1 行 1 値** → `int(input())`
- **1 行 複数値** → `map(int, input().split())`
- **複数行** → リスト内包表記 `[... for _ in range(N)]`
- **高速処理** → `sys.stdin.readline`

これらを覚えておくと、競技プログラミングの入力処理で迷わなくなります。