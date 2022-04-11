# Diabetes/Heart_disease Dtection web api
## Table of Content
* [Demo](#demo)
* [Overview](#overview)
* [Motivation/Purpose](#Motivation/Purpose)
* [Technical Aspect](#technical-aspect)
* [Evaluation matrix](#evaluation-matrix)
* [Installation](#installation) 
* [Run](#run)
* [Deployement on Heroku](#deployement-on-heroku)
* [Directory Tree](#directory-tree)
* [Technologies Used](#technologies-used)
* [Team](#team)
* [License](#license)

## Demo
Link:--><br>
https://quick-health-checkup-api.herokuapp.com
<br><br>

![20200730_134813](https://user-images.githubusercontent.com/64481847/88899511-c5cb7380-d26b-11ea-9a79-f11e39dfad0a.gif)




![](https://forthebadge.com/images/badges/made-with-python.svg) [![forthebadge](https://forthebadge.com/images/badges/validated-html5.svg)](https://forthebadge.com)
## Overview
Simple Flask app for Diabetes and Heart patient to monitor/check their health status. <a href="https://www.kaggle.com/akhileshdkapse/starter-guide-eda-acc-87-precision-92">Model1</a> (`diabetes_pima.pkl`) trained over diabetes <a href="https://www.kaggle.com/uciml/pima-indians-diabetes-database">dataset</a> and Model2 (`Heart_model_final.pkl`) is trained over heart disease <a href="https://www.kaggle.com/ronitf/heart-disease-uci">dataset</a>. To make use of this web app you must fill up respected form with valid inputs and boom!!..Model will predict and comment it out with proper guidance/advice about your health results, which will definitely make your health bettter. 
<br>
<strong>Routes Distribution...</strong><br>
<strong>Check for diabete page:</strong><br>
          This is a ML oriented Web Application for detection of the diabetes based on the parameters that the user enters.
          <br>
<strong>Check for heart disease page:</strong><br>
          This is a ML oriented Web Application for detection of presence of heart disease based on the parameters that the user enters.
          <br>
<strong>Covid page:</strong><br>
          Page specially design for reminding people to do their duty well. Alse for thanking special people on this earth !

## Motivation/Purpose
   - **Now in this pandemic situation of covid 19, there is a high risk of getting covid affected if we go out for health check-ups specially in Hospitals serving as a Covid centers. To stop the spread out this virus we have to be in home.** Taking this thought in an account, I have made this small and effective web app which will somehow contribute in making yhe world safe and healthy!  
   - Want to contribute in Medical/Health sector by providing simple, easy to use web api for detecting diabetes and presence of heart disease which can easily practised by a person working in this sector.

## Technical Aspect
This project is divided into Three part:
1.  Use of machine learning techniques to fit our data and Hypertune model parameters for its better performance.(*Jump to traning model part by clicking on Model1 in Overview section*)
2. Downloading data and our trained models(`.pkl file formate`) from kaggle kernels and setting up environment to run our app in local machine .
3. Building and hosting a Flask web app on Heroku(PAAS).

## Evaluation matrix
* <strong>Since the project aim is to predict the person is healthy or not. The trade off between models accuracy and precision.</strong>
* <strong>Due to less data, Using ANN for traning giver quite decent performance on matrix.</strong>
* <strong>Used various ML algorithms to optimize evaluation matrix.</strong>
* <strong>Model(Random forest ML algo.) gives **87%** overall accuracy,with **93%** of precision-in other words, when model predicts a person is unhealthy, it is correct 93% of the time.</strong><br>


![_Pima_Indian _ Kaggle - Google Chrome 7_23_2020 6_46_40 PM](https://user-images.githubusercontent.com/64481847/88678825-7a4e8380-d10c-11ea-9c9d-e04057860ab8.png)


## Installation
The Code is written in Python 3.7 in an anaconda environment. For anaconda instalation click <a href="https://www.anaconda.com/products/individual">here</a>.To make new environment in anaconda run following commands in your **Anaconda Prompt**.
```
conda create -n your_env_name python=3.7.x
```

## Run
After successfully creating anaconda environment, install the required packages and libraries by running this command in the project directory after cloning the repository:
```
pip install -r requirements.txt
```
then by running the following command, it will host this page in your local port and will also give you local link, which you can put in any web browser.
```
python app.py
``` 

## Deployement on Heroku
Vist <a href="Deployement on Heroku">here</a> for details.

## Directory Tree
```
├── templates
│   ├── Base.html
│   ├── home.html
│   ├── diabetes.html
│   ├── heart.html
│   └── covid.html
├── static
│   ├── images.jpg/.png/.gif
├── app.py
├── Heart_model_final.pkl
├── diabetes_pima.pkl 
├── diabetes_scaler.bin
├── diabetes.py
├── heart_mod.py
├── .gitignore
├── README.md
├── requirements.txt
├── LICENSE
├── Procfile
└──README.md
```

## Technologies Used
<img target="_blank" src="https://miro.medium.com/fit/c/1838/551/1*Ab299OETAeuTEiGg5TwpMQ.png" width=400>
<img target="_blank" src="https://softwareengineeringdaily.com/wp-content/uploads/2016/09/scikit-learn-logo.png" width=400>
<br><img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=270><img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280><img target="_blank" src="https://kazoo.jp/wpkazoo2019/wp-content/uploads/2018/05/bootstrap4.png" width=270>

## Team

<a href="https://www.linkedin.com/in/akhilesh-kapse-a8a606195/">Akhilesh Kapse</a>

## License
![MIT license](https://img.shields.io/badge/License-MIT-brightgreen)
<br>
**Copyright (c) 2020 Akhilesh kapse** <br>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:<br>
**The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.**


