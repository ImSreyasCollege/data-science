print("SJC23MCA-2053 : SREYAS SATHEESH")
print("Batch : MCA 2023-25\n")

from nltk import ngrams
sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)