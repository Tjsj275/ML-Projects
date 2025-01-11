import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

"""IMPORT DATA"""
data=pd.read_csv('movie_review.csv')
#print(data.head())

X=data.iloc[:,-2]
Y=data.iloc[:,-1]

""""TRAINING AND TESTING"""
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.20,random_state=1)

""""FEATURE EXTRACTION"""
""""Text to document matrix"""
#from sklearn.feature_extraction.text import CountVectorizer
#vectorizer=CountVectorizer()
#corpus=['This is the first document',
#        'This is the second document',
#        'And the third one',
#        'Is this the first document?']
#X=vectorizer.fit_transform(corpus)
#print(X)

""""Tfidf"""
#from sklearn.feature_extraction.text import TfidfVectorizer
#vectorizer=TfidfVectorizer()
#corpus=['This is the first document',
#        'This is the second document',
#       'And the third one',
#       'Is this the first document?']
#X=vectorizer.fit_transform(corpus)
#print(vectorizer.get_feature_names_out())
#print(X.toarray())

from sklearn.svm import LinearSVC

""""BUILDING TEXT CLASSIFIER WITH PIPELINE"""
from sklearn.pipeline import Pipeline
text_clf=Pipeline([
    ('tfidf',TfidfVectorizer()),
    ('clf',LinearSVC())
])

text_clf.fit(X_train,y_train)
y_pred=text_clf.predict(X_test)
asc=accuracy_score(y_pred,y_test)
#print(asc)

y_pred=text_clf.predict(['Amazing movie,must watch'])
#print(y_pred)



