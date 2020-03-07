# Disaster Response NLP Pipeline

# Motivation
Built an end-to-end NLP pipeline to classify social media messages in an event of a disaster to help disaster response organizations best allocate their resources and take effective actions. The datasets are provided by FigureEight, which contain pre-labeled tweets and text messages generated in events of real-life disasters.

The project consists of three parts:
- ETL(Extract, Transform, Load) pipeline: transform and merge source data into a single workable dataset
- Machine Learning pipeline: tokenized and normalized raw text data, extracted features, and built a Machine Learning model to classify message into 36 disaster categories
- Flask Web Application: showcase interactive visuals from the dataset as well as classify ad-hoc user inputs

### Instructions:
1. Run the following commands in the project's root directory to set up your database, train and save the model, and run the web app

    - Run the ETL pipeline that cleans raw data and stores into a database
        ```
        python data/ETL_pipeline.py data/messages.csv data/categories.csv data/responses.db
        ```
    - To run ML pipeline that trains classifier and saves
        ```
        python models/train_classifier.py data/responses.db models/classifier.pkl
        ```

2. cd into the app's directory, and run the web app
    ```
    python run.py
    ```

3. Go to http://0.0.0.0:3001/
