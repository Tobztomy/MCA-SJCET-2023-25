print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
from nltk import ngrams, trigrams

sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)