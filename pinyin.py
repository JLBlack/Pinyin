#!/bin/usr/env python3

import random

try: input = raw_input
except: pass
# keyword:[def1, def2, def3, correct_def_ix]
# could use module pickle to dump/load this dictionary
mydict = {
0-100 = ''
'sun' : ['black', 'yellow', 'blue', 1],
'water' : ['red', 'white', 'blue', 2],
'grass' : ['white', 'green', 'orange', 1],
'coal' : ['black', 'purple', 'red', 0]
}
keyword_list = list(mydict.keys())
random.shuffle(keyword_list)
print('Pick the right character:')
correct = 0
wrong = 0
for keyword in keyword_list:
    sf = '''\
{}
A) {}
B) {}
C) {}
'''
    print(sf.format(keyword, mydict[keyword][0],
                    mydict[keyword][1],mydict[keyword][2]))
    letter = input("Enter pinyin here: ").upper()
    if letter == 'ABC'[mydict[keyword][3]]:
        print('correct')
        correct += 1
    else:
        print('wrong')
        wrong += 1
    print('-'*30)
sf = "Answers given --> {} correct and {} wrong"
print(sf.format(correct, wrong))