# import libraries
import sys
import nltk
import re
import numpy as np
import pandas as pd
import joblib
import time
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
import warnings
warnings.filterwarnings('ignore')

def load_data(database_filepath):
    '''
    Input:
        database_filepath: the database filepath
    Output:
        X: the training data
        Y: the labels
        category_names: the name of the categories
    '''

    # load data from the database
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql('df', engine)

    # extract values from X and y
    X =  df['message'].values
    Y = df.iloc[:, 3:].values
    category_names = list(df.columns[3:])

    return X, Y, category_names


def tokenize(text):
    '''
    Input:
        text: raw message data for tokenization
    Output:
        clean_tokens: result list of tokens
    '''

    # normalize the text
    text = re.sub(r'[^a-zA-Z0-9]',' ', text.lower())
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words("english")]

    # stemming and lemming
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []

    for t in tokens:
        clean_t = lemmatizer.lemmatize(t).strip()
        clean_tokens.append(clean_t)

    return clean_tokens

def build_model():
    '''
    Build a ML pipeline that process the text and performs muilti-output classification
    on the 36 categories in the database

    Input:
        None
    Output:
        cv: GridSearch model result
    '''

    # build the pipeline
    pipeline = Pipeline([
        ('text_pipeline', Pipeline([
            ('vect', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer())
        ])),
        ('clf', MultiOutputClassifier(AdaBoostClassifier()))
    ])
    # use grid search to find better parameters
    parameters = {
        'clf__estimator__n_estimators': [10, 50],
        'clf__estimator__learning_rate': [0.1, 1],
    }

    cv = GridSearchCV(pipeline, param_grid=parameters)

    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    '''
    Input:
        model: the pipeline we built in the previous function
        X_test: test set for X
        Y_test: test set for Y
        category_names: the names of the categories

    Output:
        print the average accuracy score & F1 score of predictions across all 36 categories
    '''

    # predict on test data
    Y_pred = model.predict(X_test)

    for index, name in enumerate(category_names):

        print(f'For category - {name}')
        print(f'Accuracy score: {np.mean(accuracy_score(Y_pred[:,index], Y_test[:,index]))}')
        print(f'F1 score: {np.mean(f1_score(Y_pred[:,index], Y_test[:,index]))}')
        print('\n')

    average_accuracy_score = np.mean([accuracy_score(Y_pred[:,i], Y_test[:,i]) for i in range(len(category_names))])
    average_f1_score = np.mean([f1_score(Y_pred[:,i], Y_test[:,i]) for i in range(len(category_names))])
    print(f'The average accuracy score is {average_accuracy_score}')
    print(f'The average F1 score is {average_f1_score}')
    print('\n')



def save_model(model, model_filepath):
    '''
    Save the model to the model_filepath
    '''

    #export the model using pickel
    joblib.dump(model, model_filepath)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        start = time.time()
        model.fit(X_train, Y_train)
        print(f'The model trained for {round(time.time() - start,2)} seconds')

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')
        print('Best Estimator: \n')
        print(model.best_estimator_)

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
