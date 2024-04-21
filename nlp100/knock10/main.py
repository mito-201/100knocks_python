"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""
import subprocess
import sys

args = sys.argv

print(args)

print(len(open(args[1]).readlines())) 

cmd = "wc -l " + args[1]
print(subprocess.check_output(cmd.split()).decode().split()[0])