import pandas as pd 
import nltk
import re
import spacy

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class Preprocessing:

    def __init__(self):
        self.fake_news_dataset = pd.read_csv("data/Fake.csv")
        self.true_news_dataset = pd.read_csv("data/True.csv")
        self.stops = stopwords.words('english')
        self.spc = spacy.load('en_core_web_sm')

        nltk.download('punkt')
        nltk.download('stopwords')
    
    def csv_head(self, dataset):
        """ 
        Prints the first 5 rows of each dataset 
        """
        print(dataset.head())

    def tokenize(self, text):
        """ 
        Tokenizes the text 
        """
        return word_tokenize(text)

    def only_lowercased_letters(self, text):
        """ 
        Removes all punctuation from the text and
        lowercases all words and letters
        """
        return re.findall(r'\b[A-zÀ-úü]+\b', text.lower())

    def remove_stopwords(self, text):
        """
        Removes all stopwords from a text
        """
        no_stopwords = [word for word in text if word not in self.stops]
        important_words = " ".join(no_stopwords)
        return important_words

    def lemmatize(self, important_words, tokens):
        """
        Lemmatizes important words
        """
        spc_words = self.spc(important_words)
        lemmas = [tokens.lemma_ if tokens.pos_ == 'VERB' else str(tokens) for tokens in spc_words]
        clean_text = " ".join(lemmas)
        return clean_text

    def clean_text(self, text):
        print("Tokeninzing . . .")
        token = self.tokenize(text)

        print("Removing stop words . . .")
        important_words = self.remove_stopwords(self.only_lowercased_letters(text))

        print("Lemmas . . .")
        lemmas = self.lemmatize(important_words, token)

        return lemmas

