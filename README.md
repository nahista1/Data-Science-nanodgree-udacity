## 1 - Data Science Blog Post


### Libraries
To be able to run this notebook, you need to install these libraries:
- [Pandas](https://github.com/pandas-dev/pandas)
- [Seaborn](https://github.com/mwaskom/seaborn)
- [Matplotlib](https://github.com/matplotlib/matplotlib)

### Introduction
In this project, I did the analysis for Stack Overflow Survey Data 2019. This is a survey data which I took from their [website](https://insights.stackoverflow.com/survey). This data contains nearly 90,000 responses from over 170 countries. I used jupyter notebook to do the analysis which you can find in the `Data Science Blog Post.ipynb` file.
<br>
<br>
For this analysis, I focused in answering these three questions:
1. In Which country has the highest job satisfaction for developers ?
2. What is the difference in job satisfaction between developers whose undergraduate major is IT-related an those who are not ?
3. Is there any differences in terms of salary between people who contribute to open source and those who are not?

### Result Summary
After I did the analysis, these are the conclusion I found:
1. United States has the highest job satisfaction level for developers in the world, and 5 of top 10 countries with the highest job satisfaction level are located in Europe.
2. Developers whose undergraduate major is not IT-related have slightly better job satisfaction.
3. Developers who contribute more to the open source have the higher salary (although ”does it have the direct causation?” is still debatable).

.


## 2 - ML-Model-Flask-Deployment
This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :

1. model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
 
 This would create a serialized version of our model into a file model.pkl
2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000
4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```


