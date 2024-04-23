"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
import subprocess
import sys

args = sys.argv
text = open(args[1]).read().replace("\t", " ")
print(text)

text2 = subprocess.run("sed 's/\t/ /' popular-names.txt", shell=True)
print(text2)