import pandas as pd 

class Analysis:

    def __init__(self):
        self.fake_news_dataset = pd.read_csv("data/Fake.csv")
        self.true_news_dataset = pd.read_csv("data/True.csv")
    
    def csv_head(self):
        print(self.fake_news_dataset.head())
        print(self.true_news_dataset.head())
