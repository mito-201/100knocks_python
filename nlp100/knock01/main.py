"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

string = 'パタトクカシーー'
string1 = ''

for i in range(0, len(string), 2):
    string1 = string1 + string[i]

print(string1)
    