# Disaster Response NLP Pipeline

# Motivation
Built an end-to-end NLP pipeline to classify social media messages in an event of a disaster to help disaster response organizations best allocate their resources and take effective actions. The datasets are provided by FigureEight, which contain pre-labeled tweets and text messages generated in events of real-life disasters.

The project consists of three parts:
- ETL(Extract, Transform, Load) pipeline: transform and merge source data into a single workable dataset
- Machine Learning pipeline: tokenized and normalized raw text data, extracted features, and built a Machine Learning model to classify message into 36 disaster categories
- Flask Web Application: showcase interactive visuals from the dataset as well as classify ad-hoc user inputs

# Execution
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

# Dependencies
- Click==7.0
- Flask==1.1.1
- itsdangerous==1.1.0
- Jinja2==2.11.1
- joblib==0.14.1
- MarkupSafe==1.1.1
- nltk==3.4.5
- numpy==1.18.1
- pandas==1.0.1
- plotly==4.5.3
- python-dateutil==2.8.1
- pytz==2019.3
- retrying==1.3.3
- scikit-learn==0.22.2.post1
- scipy==1.4.1
- six==1.14.0
- sklearn==0.0
- SQLAlchemy==1.3.13
- Werkzeug==1.0.0


# Flask Web App
![alt text](https://github.com/kevingao1136/DataScience_Udacity/blob/master/Disaster_Response_Project/screenshots/Screen%20Shot%202020-03-07%20at%203.44.47%20PM.png)
![alt text](https://github.com/kevingao1136/DataScience_Udacity/blob/master/Disaster_Response_Project/screenshots/Screen%20Shot%202020-03-07%20at%204.53.37%20PM.png)
