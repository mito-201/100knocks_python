"""
00. 文字列の逆順
文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

string = 'stressed'
string1 = ''

for i in range(len(string) - 1, -1, -1):
    string1 = string1 + string[i]

print(string1)
