from classification.preprocessing import Preprocessing
from data.mongo import Mongo
import pandas as pd
import logging

class Corgi4News:

    def __init__(self):
        self.preprocessing = Preprocessing()
        self.mongo = Mongo()
        self.fake_news = self.preprocessing.fake_news_dataset
        self.real_news = self.preprocessing.real_news_dataset

        self.preprocessing_and_saving_data(
            self.fake_news, 'fake_news', 'title', 'clean_title', 'title')
        self.preprocessing_and_saving_data(
            self.real_news, 'real_news', 'title', 'clean_title', 'title')
        self.preprocessing_and_saving_data(
            self.fake_news, 'fake_news', 'text', 'clean_text', 'title')
        self.preprocessing_and_saving_data(
            self.real_news, 'real_news', 'text', 'clean_text', 'title')

    def preprocessing_and_saving_data(self, df, collection_name, raw_column_name, new_column_name, query_data):
        """
        Applies preprocessing function on a certain column
        of a certain dataframe and stores the preprocessed
        data on a new column in the respective MongoDB
        collection of this dataframe.

        df = dataframe
        collection_name = name of the mongodb collection
        raw_column_name = name of the column that contains 
        raw data
        new_column_name = name of the column that will store 
        preprocessed data
        query_data = data that will be used in the query to 
        store preprocessed data in the correct index
        """

        df[new_column_name] = df[raw_column_name].apply(self.preprocessing.clean_text)
        try:
            for index in range (len(df)):
                self.mongo.insert_into_collection(
                    df[query_data][index],
                    collection_name, 
                    new_column_name, 
                    df[new_column_name][index]
                )
            print("*****************************************")
            print(f"{collection_name} {new_column_name} done.")
            print("*****************************************")
        except Exception as e:
            logging.error('Failed to upload: '+ str(e))
     
if __name__ == "__main__":
    corgi4news = Corgi4News()