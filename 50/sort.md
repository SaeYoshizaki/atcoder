```python
配列名.sort()
```

で使用できる。

この場合、ソートの順番は昇順となる。

降順にしたい場合は、

```python
配列名.sort(reverse = True)
```

とすればOK

この関数の計算量は、配列の長さがNだった場合、Nlog(N)となる。
時と場合に応じては、TELするので注意。

二次元配列のときは、要素の最初の方がソートの対象として使われる。

例えば、

```python
[[2846, 'QCFium'], [2992, 'chokudai'], [2390, 'penguinman'], [2432, 'kyoprofriends']]
```

こういう配列の場合は、前の要素、つまり、数値を元にソートが行われ、

配列名.sort(reverse=True)

をすると、

```python
[[2992, 'chokudai'], [2846, 'QCFium'], [2432, 'kyoprofriends'], [2390, 'penguinman']]
```

と書き直すことができる。

文字と数字が逆の場合は、アルファベット順にソートされる。