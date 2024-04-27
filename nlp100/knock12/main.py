"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""

import subprocess
import sys

args = sys.argv
text = open(args[1]).readlines()

col1 = []
col2 = []

for index in range(len(text)):
    col1.append(text[index].split()[0])
    col2.append(text[index].split()[1])
    
print(col1)
print(col2)




