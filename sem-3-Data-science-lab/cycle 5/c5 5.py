import nltk
from nltk import ngrams
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
from nltk.tokenize import sent_tokenize, word_tokenize
text1 = "The data given satisfies the requirement for model generation. This is used in Data Science Lab"
print("Sentance tokeniztion : ")
print(sent_tokenize(text1))
text = word_tokenize(text1)
text2 = [word for word in text if word not in stopwords.words('english')]
print("")
print("Removing stop words : ")
print(text2)
print("")
print("n grams : ")
unigrams = ngrams(text2,3)
for grams in unigrams:
    print(grams)