# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine

def process_data(messages_filepath, categories_filepath):
    '''
    Process and merge messages and categories data into df

    Input:
        messages_filepath: the filepath for the messages data
        categories_filepath: the filepath for the categories data

    Output:
        df: merged data with messages and categories they belong to
    '''

    # Load datasets and remove duplicates
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    messages.drop_duplicates(inplace=True, subset='id')
    categories.drop_duplicates(inplace=True, subset='id')

    # Test that the two datasets have the same ids without duplicates
    assert set(messages.id) == set(categories.id), 'ids of two datasets do not match'
    assert len(messages) == len(categories), 'length of two datasets do not match'

    # Clean and Transform categories data
    df = pd.merge(messages, categories, on='id')
    categories = df.categories.str.split(';', expand = True)
    col_names = categories.iloc[0,:].apply(lambda x: x[:-2])
    categories.columns = col_names
    categories.related.loc[categories.related == 'related-2'] = 'related-1'
    for col in categories:
        categories[col] = categories[col].str[-1]
        categories[col] = categories[col].astype(int)

    # Test that categories data is correctly encoded into only 0 and 1
    assert ((categories == 0) | (categories == 1)).all().all(), 'data has values other than 1 and 0'

    # Merge the data
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df,categories], axis=1)
    df.drop('original',axis=1,inplace=True)

    # Test for duplicates and null values in df
    assert not df.duplicated().any(), 'duplicates in df'
    assert not df.isnull().any().any(), 'null values in df'

    return df

def save_data(df, database_filename):
    '''
    Save dataframe to database in
    '''
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('df', engine, if_exists='replace', index=False)

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = process_data(messages_filepath, categories_filepath)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')

if __name__ == '__main__':
    main()
