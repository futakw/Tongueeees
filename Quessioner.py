import pickle
import numpy as np
import random 

ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("dictionary.pkl", "rb") as f:  # "dictionary.pkl" is available from 
    dictionary = pickle.load(f)                 # http://ushitora.net/archives/456
f.close()                                # The list of 153,484 words in about 100 books.

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

class TonguessQuestioner:
    def __init__(self, dictionary, word_len):
        self.word_len = word_len
        self.dictionary = [w for w in dictionary if '-' not in w and len(w)==word_len]
        self.ans_word = random.choice(self.dictionary).upper()
        print(self.ans_word)
        self.count = 1
        
    def question(self, word):
        word = word.upper()
        if len(word) != self.word_len:
            print('Wrong length ! ')
            return False, None
        if len(word)!=len(set(word)):
            print('Same letter exists ! ')
            return False, None
        
        Eat = 0
        Bite = 0
        for i in range(len(word)):
            if word[i] == self.ans_word[i]:
                Eat += 1
            elif word[i] in self.ans_word:
                Bite += 1
        feedback = [word, Eat, Bite, self.count]
        
        if Eat == self.word_len:
            print('Correct!!!  ---> Tried Time : ', self.count)
            print('The answer is :' , self.ans_word)
            return True, feedback
        else:
            print('Eat : {} , Bite : {}'.format(Eat,Bite))
            self.count += 1
            return False, feedback
    
    
print('Input the Length of word')
word_len = input('>>>')

print("OK, Let's Start this Game :) " )
print('Word length : ' , word_len)
print('------------------------------------------------ ')

H = TonguessQuestioner(dictionary, int(word_len) )
while True:
    print('Input the word')
    w = input('>>>')
    _ = H.question(w)          
    if _ : break