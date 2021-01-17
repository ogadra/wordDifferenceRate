import sys
import re
import MeCab
mecab = MeCab.Tagger('-Owakati')

text = open('hitofusano_budo.txt').read()
text = re.sub('［.*］', '', text)
text = re.sub('《.*》', '', text)
text = re.sub('\n| |　', '', text)
text = mecab.parse(text)

textList = text.split(' ')
textSet = set(textList)
print(len(textSet) / len(textList))