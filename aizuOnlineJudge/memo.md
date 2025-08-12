# 約数の求め方
```python
divisor = list(i for i in range(1, c + 1) if c % i == 0)
```

# floatで出力の桁数を制限する方法
https://trends.codecamp.jp/blogs/media/column221
```python
result = "{:.5f}".format(A)
# これで小数点第5桁までとなる。
```