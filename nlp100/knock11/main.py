"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
import subprocess
import sys

args = sys.argv

print(len(open(args[1]).readlines())) 

cmd = "wc -l " + args[1]
print(subprocess.check_output(cmd.split()).decode().split()[0])