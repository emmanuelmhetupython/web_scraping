import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
with open('eunice.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        example_text = row[0]
        tokenized = word_tokenize(example_text)
        print(tokenized)






































