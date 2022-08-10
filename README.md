# Data_engineering_practice

This is a solution to the Data Engineering Pracice Repository for the [data engineering course ](https://github.com/DataTalksClub/data-engineering-zoomcamp) by Data Talks.  

## Table of contents

- [Overview](#overview)
  - [The Coursework.](#the-challenge)
  - [Links](#links)
- [Tools and Featured Works](#my-process)
  - [Tools](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)


## Overview

### The Coursework

Dream Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan. The solution will then have to automate the process of checking eligibility of an applcant by the data provided online.


### Links

- Solution URL: [My Project](https://github.com/kariswanjiru/loan-prediction-hackathon)

## Tools and Featured work

### Tools :

- GCP
- Docker
- Terraform
- Postgressql
- Python

### What I learned

I learnt how to use stratified k-folds to better the accuracy of my machine learning algorithm.

This is a code snippet of what i learnt, see below:

```python
i = 1 
kf = StratifiedKFold(n_splits=5,random_state=1,shuffle=True)
for train_index,test_index in kf.split(x , y):
    print('{} of kfold {}'.format(i,kf.n_splits))
    xtr,xvl = x.iloc[train_index],x.iloc[test_index]
    ytr,yvl = y.iloc[train_index],y.iloc[test_index]
    model = LogisticRegression(random_state=1)
    model.fit(xtr,ytr)
    pred_test = model.predict(xvl)
    score = accuracy_score(yvl,pred_test)
    print('accuracy_score',score)
    i+=1
    pred_test = model.predict(test)
    pred = model.predict_proba(xvl)[:, 1]
    
```

### Continued development
For my next projects I will improve my accuracy using feature engineering and boosting algorithis like Adaboost.  

### Useful resources

- [Skit-learn](https://scikit-learn.org/stable/) - This helped me with deeper understanding of the use of skit-lern models.
- [Pandas](https://pandas.pydata.org/docs/) - Pandas docuentation.



## Author

- LinkedIn - [Wanjiru Kariuki](https://www.linkedin.com/in/wanjiru-kariuki/)
- Twitter - [@Wanjiruestar](https://www.twitter.com/Wanjiruestar)

