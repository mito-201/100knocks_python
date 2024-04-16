"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

def get_word_n_gram(num, string):
    result = {}
    start = 1
    print(len(string.split()))
    while (start + num) <= len(string.split()):
        for word in string.split():
            result = word
        start += 1
    return result

# def get_char_n_gram(num, string):
    
string = "I am an NLPer"

res = get_word_n_gram(1, string)

print(res)