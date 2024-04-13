"""
04. 元素記号
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dict = {} 

id = 1
for word in string.split():
    dict[id] = word
    id += 1

for id in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
    dict[id] = dict[id][0]

for id in [2, 3, 4, 10, 11, 12, 13, 14, 17, 18, 20]:
    dict[id] = dict[id][0:2]

print(dict)
