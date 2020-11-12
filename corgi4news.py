from classification.preprocessing import Preprocessing
import pandas as pd


preprocessing = Preprocessing()

fake_news = preprocessing.fake_news_dataset
true_news = preprocessing.true_news_dataset

fake_news['Clean title'] = fake_news['title'].apply(preprocessing.clean_text)
# fake_news['Clean text'] = fake_news['text'].apply(preprocessing.clean_text)
# true_news['Clean title'] = true_news['title'].apply(preprocessing.clean_text)
# true_news['Clean text'] = true_news['tile'].apply(preprocessing.clean_text)

preprocessing.csv_head(fake_news)
preprocessing.csv_head(true_news)