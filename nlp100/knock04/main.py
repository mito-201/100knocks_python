"""
04. 元素記号
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dict = {} 

for word in string.split():     # wordには、１要素の文字列が入る
    count = 0
    for char in word:           # charには、1文字ずつ入る
        if char.isalpha():      # アルファベット判定を行う
            count += 1
    result.append(count)        # listに追加する

for id in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
    dict[id] = string.split()

print(dict)