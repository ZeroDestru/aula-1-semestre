import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

t1 = input("Resposta 1")
t2 = input("Resposta 2")

vect = CountVectorizer(analyzer = 'word', ngram_range= (1, 2))
vocab = vect.fit([t1, t2])

textos = vect.fit_transform([t1, t2]) 
textos = test.toarray() #transformando em array para olhar a matriz
print(test)
vocab.vocabulary_