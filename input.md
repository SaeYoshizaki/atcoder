# 色々なinputのやり方
- 複数行にわたる文字列を一つのリストで受け取る
```python
inputArr = [input() for _ in range(n)]
# nは入力の行数
```

- 1行で複数の数値を受け取る
``` python
A, B, C = map(int, input().split())
```

- 文字列をリストとして受け取る
```python
StrArr = list(input())
```