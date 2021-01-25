import sys
import re
import MeCab
mecab = MeCab.Tagger('-Owakati')

text = open('hitofusano_budo.txt').read()
text = re.sub('［[^［］]*］', '', text)
text = re.sub('《[^《》]*》', '', text)
text = re.sub('\n| |　', '', text)
text = re.sub('。|、', ' ', text)
text = mecab.parse(text)

print(text)

textList = text.split(' ')
textSet = set(textList)


print(len(textSet) / len(textList))
print(len(textSet), len(textList))   
#理想値 674 / 3806
#実数値 809 / 3765
# 0.2148738379814077