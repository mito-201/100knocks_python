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

# 2.7.1. 繰り返し（for 文
for i in range(5):
    print(i)
print(i)

names = ['佐藤', '鈴木', '高橋']
for i in range(3):
    print('{}さん'.format(names[i]))

print(len(names))

for i in range(len(names)):
    print('{}さん'.format(names[i]))

for name in names:
    print('{}さん'.format(name))

for i, name in enumerate(names):
    message = '{}番目：{}さん'.format(i, name)
    print(message)

names = ['Python', 'Chainer']
versions = ['3.7', '5.3.0']
suffixes = ['!!', '!!', '?']
for name, version, suffix in zip(names, versions, suffixes):
    print('{} {} {}'.format(name, version, suffix))

# 2.7.2. 条件分岐（if 文）
a = 1
if a > 0:
    print('0より大きいです')
else:
    print('0以下です')

a = -1
if a > 0:
    print('0より大きいです')
else:
    print('0以下です')

a = 0
if a > 0:
    print('0より大きいです')
elif a == 0:
    print('0です')
else:
    print('0より小さいです')

# 2.7.3. 繰り返し（while 文）
count = 0
while count < 3:
    print(count)
    count += 1

count = 0
while True:
    print(count)
    count += 1

    if count == 3:
            break

print(not True)
print(not False)
print(not 1 == 2)

count = 0
while not count == 3:
    print(count)
    count += 1

# 2.8.1. 関数を定義する
"""
関数 double() の定義
"""
def double(x):
    print(2 * x)
"""
関数の実行
"""
double(3)
double(5)
double(1.5)

# 2.8.2. 複数の引数をとる関数
def add(a, b):
    print(a + b)
add(1, 2)
add(3, 2.5)
add(1, -5)

# 2.8.3. 引数をとらない関数
def hello():
    print('Chainerチュートリアルへようこそ')
hello()

# 2.8.4. 引数のデフォルト値
def hello1(message='Chainerチュートリアルにようこそ1'):
    print(message)
hello1()

hello1('Welcome to Chainer tutorial')

# 2.8.5. 返り値のある関数
def add(a, b):
    return a + b
result = add(1, 3)
print(result)

result = add(1, 3)
result_doubled = result * 2
print(result_doubled)

print(add(2, 3) * add(1, 3))

# 2.8.6. 変数のスコープ
a = 1
def change():
    a = 2
change()
print(a)

a = 1
def change():
    print('From inside:', a)
change()
print('From outside:', a)

a = 1
def change():
    global a  # a をグローバル変数である宣言
    a = 2
change()
print(a)    # 結果の確認 <- a の値が上書きされている

# 2.9.1. クラスの定義
"""クラスの定義"""
class House:
    def __init__(self, name):  # __init__()は、インスタンス化する際に自動的に呼ばれるメソッド
        self.name_plate = name

my_house = House('Chainer')
print(my_house.name_plate)

class House:
    def __init__(self, name):
        self.name_plate = name
    
    def hello(self):
        print('{}の家です'.format(self.name_plate))

sato = House('佐藤')
suzuki = House('スズキ')
sato.hello()
suzuki.hello()

# 2.9.2. 継承
class Link:
    def __init__(self):
        self.a = 1
        self.b = 2
l = Link()
print(l.a)
print(l.b)

class Chain(Link):
    def sum(self):
        return self.a + self.b
c = Chain()
print(c.a)
print(c.b)
print(c.sum())

"""
# エラーの確認
class Chain(Link):
    def __init__(self):
        self.c = 5
    
    def sum(self):
        return self.a + self.b + self.c

C = Chain()
print(C.sum())

# エラーメッセージ
Traceback (most recent call last):
  File "/workspaces/100knocks_python/ChainerTutorial/2.py", line 366, in <module>
    print(C.sum())
          ^^^^^^^
  File "/workspaces/100knocks_python/ChainerTutorial/2.py", line 363, in sum
    return self.a + self.b + self.c
           ^^^^^^
AttributeError: 'Chain' object has no attribute 'a'
"""

class Chain(Link):
    def __init__(self):
        super().__init__()
        self.c = 5
    
    def sum(self):
        return self.a + self.b + self.c

C = Chain()
print(C.sum())

class MyNetwork(Chain):
    def mul(self):
        return self.a * self.b * self.c
net = MyNetwork()
print(net.mul())
