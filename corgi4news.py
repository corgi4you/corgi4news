from classification.preprocessing import Preprocessing
from data.mongo import Mongo
import pandas as pd

preprocessing = Preprocessing()
mongo = Mongo()

fake_news = preprocessing.fake_news_dataset
real_news = preprocessing.real_news_dataset

def preprocessing_and_saving_data(self, df_name, raw_column, new_column, query_data):
    """
    Applies preprocessing function on a certain column
    of a certain dataframe and stores the preprocessed
    data on a new column in the respective MongoDB
    collection of this dataframe.

    df_name = dataframe/collection name
    raw_column = name of the column that contains 
    raw data
    new_column = name of the column that will store 
    preprocessed data
    query_data = data that will be used in the query to 
    store preprocessed data in the correct index
    """

    df_name['new_column'] = df_name['raw_column'].apply(preprocessing.clean_text)
    for index in range (len(df_name)):
        mongo.insert_into_collection(df_name['query_data'][index],
        "df_name", "new_column", df_name['new_column'][index])
    print(f"{df_name} {new_column} done")
