import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer # unsupervised sentence tokenizer but you can train it if you want.
with open('Allheadlines.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        example_text = row[0]
        All_lowercase = example_text.lower()
        tokenized = word_tokenize(All_lowercase)
        stop_words = set(stopwords.words("English"))
        filtered_sentence = [w for w in tokenized if not w in stop_words]
        train_text = state_union.raw("2005-GWBush.txt")
        sample_text = state_union.raw("2006-GWBush.txt")
        custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
        tokenizedd = custom_sent_tokenizer.tokenize(sample_text)
        def process_content():
            try:
                for i in filtered_sentence:
                    words = nltk.word_tokenize(i)
                    tagged = nltk.pos_tag(words)
                    chunkGram = """ Chunk:{<RB.?>*<VB.?>*<NNP><NN>?} """
                    chunkParser = nltk.RegexpParser(chunkGram)
                    chunked = chunkParser.parse(tagged)
                    print(chunked)
            except Exception as e:
                    print(str(e))
        process_content()
        
                    
