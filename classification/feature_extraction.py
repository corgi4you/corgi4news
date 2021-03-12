from sklearn.feature_extraction.text import CountVectorizer

class FeatureExtraction:

    def __init__(self):
        return

    def bag_of_words(self, df_clean_text):
        count_vectorizer = CountVectorizer()
        return count_vectorizer.fit_transform(df_clean_text)

    def wordclouds(self):
        return

    def tf_idf(self):
        return

    def ngrams(self):
        return
