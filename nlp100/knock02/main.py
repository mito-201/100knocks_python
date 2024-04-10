"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

string = ''
string1 = 'パトカー'
string2 = 'タクシー'


for i in range(0, len(string1), 1):
    string = string + string1[i]
    string = string + string2[i]

print(string)