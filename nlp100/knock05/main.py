"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

def get_n_gram(num, string):
    return [ string[idx:idx + num] for idx in range(len(string) - num + 1)]
 
string = "I am an NLPer"

print(get_n_gram(2, string))
print(get_n_gram(3, string))
print(get_n_gram(4, string))

words = string.split(' ')

print(get_n_gram(2, words))
print(get_n_gram(3, words))
print(get_n_gram(4, words))
