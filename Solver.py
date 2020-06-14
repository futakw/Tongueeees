import pickle
import numpy as np
import random 

ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("dictionary.pkl", "rb") as f:  # "dictionary.pkl" is available from 
    dictionary = pickle.load(f)                 # http://ushitora.net/archives/456
f.close()                                # The list of 153,484 words in about 100 books.

# https://www.wordfrequency.info/files/entriesWithoutCollocates.txt より
"""
dictionary = []
path = './words_list.txt'
with open(path) as f:
    for s_line in f:
        l = s_line.split()
        dictionary +=[ l[1]]
"""
        
dictionary = [w for w in dictionary if len(w)==len(set(w))]
d = []
for w in dictionary:
    ok = True
    for s in w:
        if s.upper() not in ALPHA:
            ok = False
    if ok:
        d += [w]
dictionary = d    


class TonguessSolver:
    def __init__(self, dictionary, word_len):
        self.word_len = word_len    
        self.data = []
        self.delete_letter = []
        self.my_dictionary = [w for w in dictionary if '-' not in w and len(w)==word_len]
            
    def guess(self):
        w = random.choice(self.my_dictionary)
        return w.upper()
        
    def feedback(self, feedback ):
        word, Eat, Bite, count = feedback
        print(feedback)
        self.data += [feedback]
        
        d = []
        for w in self.my_dictionary:
            w = w.upper()
            Eat_count = 0 
            Bite_count = 0
            for i in range(len(word)) :
                if word[i] == w[i]:
                    Eat_count += 1
                if word[i] != w[i] and word[i] in w:
                        Bite_count += 1
            # もし条件にそってたら           
            if Eat_count==Eat and Bite_count==Bite:
                d += [w]
        self.my_dictionary = d


print('Input the Length of word')
word_len = input('>>>')

print("OK, Let's Start this Game :) " )
print('Word length : ' , word_len)
print('------------------------------------------------ ')

S = TonguessSolver(dictionary, int(word_len) )

count = 0
while True:
    w = S.guess()
    print('Guessed word is >>>> ', w )
    count += 1
    
    while True:
        Eat = input('Input the Eat num >>>> ')
        Bite = input('Input the Bite num >>>> ')
        try:
            Eat, Bite = int(Eat) , int(Bite)
            if Eat+Bite<=S.word_len and Eat>=0 and Bite>=0:
                break
            else:
                print('Maybe wrong, try again')
        except:
            print('Maybe wrong, try again')
    
    feedback = [w, Eat, Bite, count]
    S.feedback(feedback)
    
    if Eat == S.word_len : 
        print('YEAHHHHHHHH !')
        break
    else:
        print('Hmm....')
        
