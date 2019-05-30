import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
with open('eunice.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        example_text = row[0]
        All_lowercase = example_text.lower()
        tokenized = word_tokenize(All_lowercase)
        stop_words = set(stopwords.words("English"))
        filtered_sentence = [w for w in tokenized if not w in stop_words]
        print(filtered_sentence)
