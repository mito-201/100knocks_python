"""
03. 円周率
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という
文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

print(string.split())  # 分割

result = []

for word in string.split():     # wordには、１要素の文字列が入る
    count = 0
    for char in word:           # charには、1文字ずつ入る
        if char.isalpha():      # アルファベット判定を行う
            count += 1
    result.append(count)        # listに追加する

print(result)