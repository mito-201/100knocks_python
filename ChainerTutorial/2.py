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

# 2.4. 文字列メソッド
name = 'Chainer'
print(name)
print(name.lower())
print(name.upper())

name = 'Chainer'
print("{} チュートリアルへようこそ".format(name))

name1 = 'Chainer'
name2 = 'チュートリアル'
print('{} {}へようこそ'.format(name1, name2))

version = 3.7
print('Python {}'.format(version))

# 2.5. 浮動小数点数がもつメソッド
print(0.5.as_integer_ratio())
print(0.25.as_integer_ratio())

# 2.6.1. リスト
numbers = [4, 5, 6, 7]
print(numbers)
print(type(numbers))

print(len(numbers))
print(numbers[0])
print(numbers[2])

numbers[1] = 10
print(numbers[1])
print(numbers)

print(numbers[-1])
print(numbers[-3])

print(numbers[0:2])
print(numbers[:2])
print(numbers[1:])
print(numbers[:])

array = ['hello', 'world']
print(array)

array = [1, 1.2, 'Chainer']
print(array)

array = [[1, 1.2, 'Chainer', True], [3.2, 'Tutorial']]
print(array)

array.append(2.5)
print(array)

array = []
array.append('Chainer')
array.append('チュートリアル')
print(array)

# 2.6.2. タプル
array = (4, 5, 6, 7)
print(array)
print(type(array))

print(array[0])
print(array[:3])

"""
array[0] = 10

Traceback (most recent call last):
  File "/workspaces/100knocks_python/ChainerTutorial/2.py", line 159, in <module>
    array[0] = 10
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

# 2.6.3. 辞書
scores = {'Math': 90, 'Science': 75, 'English': 80 }
print(scores)
print(scores['Math'])

scores = {'数学': 90, '理科': 75, '英語': 80}
print(scores)
print(scores['数学'])

print(scores.keys())
print(scores.values())
print(scores.items())

scores['国語'] = 85
print(scores)