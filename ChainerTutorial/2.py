# 2.2.1. 代入と値の確認
a = 1
print(a)
type(a)
# 2.2.2. コメント
# print(a)

# 2.2.3. 変数の型
a = 1
b = 1.2
c = 'Chainer'
print(type(a))
print(type(b))
print(type(c))

print(type(0))
print(type(0.))
print(type(.0))

print(type(5.0))
print(type(5.))

print(type(.5))
print(.5)

# 2.2.4. 複数同時の代入
a, b, c = 1, 1.2, "Chainer"
print(a)
print(b)
print(c)

# 2.2.5. 算術演算子
print(1 + 1)

a = 1
print(a + 2)

b = 0.2
print(a + b)

print(3 / 2)
print(4 // 2)

"""
a + c

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-32-e81e582b6fa9> in <module>()
----> 1 a + c

TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

"""
# str と int で乗算
print(c * 3)
"""

name1 = 'Chainer'
name2 = 'チュートリアル'
print(name1 + name2)

print(type(1))
print(type(str(1)))
print(str(1) + "番目")

count = 0
count = count + 1
print(count)
count = 0
count += 1
print(count)

print(2 ** 3)
print(9 / 2, 9 // 2, 9 % 2)

# 2.2.6. 比較演算子
print(1 < 2)
print(type(1 < 2))
print(2 == 5)
print(1 != 2)
print(3 >= 3)
print('test' == 'test')

# 2.3. エスケープシーケンス
print('Hello\nWorld')
print('Hello\tWorld')

d = 'Hello\nWorld'
print(d)