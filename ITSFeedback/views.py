from django.shortcuts import render
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import make_multilabel_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import ClassifierChain

global classifier
global i
global j

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def DetectState(request):
    if request.method == 'GET':
       return render(request, 'DetectState.html', {})


def Admin(request):
    if request.method == 'GET':
       return render(request, 'Admin.html', {})

def AdminLogin(request):
    if request.method == 'POST':
      username = request.POST.get('t1', False)
      password = request.POST.get('t2', False)
      if username == 'admin' and password == 'admin':
       context= {'data':'welcome '+username}
       return render(request, 'AdminScreen.html', context)
      else:
       context= {'data':'login failed'}
       return render(request, 'Admin.html', context)

def traintest(train):     #method to generate test and train data from dataset
    X = train.values[:, 0:6] 
    Y = train.values[:, 6:8]
    print(Y)
    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 0)
    return X, Y, X_train, X_test, y_train, y_test

def BuildModel(request):
    global classifier
    train = pd.read_csv(r'C:\Users\hi\Desktop\ITS\ITSFeedback\dataset\affect_estimates.csv')
    X, Y, X_train, X_test, y_train, y_test = traintest(train)
    X, y = make_multilabel_classification(sparse = True, n_labels = 9,return_indicator = 'sparse', allow_unlabeled = False)
    classifier = ClassifierChain(RandomForestClassifier(n_estimators=100))
    classifier.fit(X_train, y_train)
    context= {'data':'Model Theory Build on '+str(len(train))+' students data'}
    return render(request, 'AdminScreen.html', context)

def AffectState(request):
    global i
    global j
    if request.method == 'POST':
      confuse = request.POST.get('t1', False)
      concentrate = request.POST.get('t2', False)
      bore = request.POST.get('t3', False)
      frustrate = request.POST.get('t4', False)
      strdata = 'id,student,observed_5fused,observed_1age_5centrating,observed_2ed,observed_4strated\n'
      strdata = strdata+'0,72720,'+confuse+','+concentrate+','+bore+','+frustrate
      file = open(r'C:\Users\hi\Desktop\ITS\ITSFeedback\dataset\temp1.txt','w')
      file.write(strdata)
      file.close()    
      test = pd.read_csv(r'C:\Users\hi\Desktop\ITS\ITSFeedback\dataset\temp1.txt')
      predictions = classifier.predict(test)
      i = predictions[0][0]
      j = predictions[0][1]

      msg = ''
      if i == 0.0 and j == 0.0:
         msg = 'Weldone! You are performing well.'
      if i == 0.0 and j == 1.0:
         msg = 'Affected with Concentration. Motivation Message Required.'  
      if i == 0.0 and j == 2.0:
         msg = 'Getting Bored. Motivation Message Required.'  
      if i == 0.0 and j == 3.0:
         msg = 'Affected with Multiple Problems. Motivation Message Required.'  
      if i == 0.0 and j == 4.0:
         msg = 'Getting Frustrated. Motivation Message Required.' 
      if i == 0.0 and j == 5.0:
         msg = 'Looking Confused. Motivation Message Required.' 

      if i == 1.0 and j == 0.0:
         msg = 'Weldone! You are performing well.'
      if i == 1.0 and j == 1.0:
         msg = 'Affected with Concentration. Motivation Message Required.'  
      if i == 1.0 and j == 2.0:
         msg = 'Getting Bored. Motivation Message Required.'  
      if i == 1.0 and j == 3.0:
         msg = 'Affected with Multiple Problems. Motivation Message Required.'  
      if i == 1.0 and j == 4.0:
         msg = 'Getting Frustrated. Motivation Message Required.' 
      if i == 1.0 and j == 5.0:
         msg = 'Looking Confused. Motivation Message Required.' 

      if i == 2.0 and j == 0.0:
         msg = 'Weldone! You are performing well.'
      if i == 2.0 and j == 1.0:
         msg = 'Affected with Concentration. Motivation Message Required.'  
      if i == 2.0 and j == 2.0:
         msg = 'Getting Bored. Motivation Message Required.'  
      if i == 2.0 and j == 3.0:
         msg = 'Affected with Multiple Problems. Motivation Message Required.'  
      if i == 2.0 and j == 4.0:
         msg = 'Getting Frustrated. Motivation Message Required.' 
      if i == 2.0 and j == 5.0:
         msg = 'Looking Confused. Motivation Message Required.' 

      if i == 3.0 and j == 0.0:
         msg = 'Weldone! You are performing well.'
      if i == 3.0 and j == 1.0:
         msg = 'Affected with Concentration. Motivation Message Required.'  
      if i == 3.0 and j == 2.0:
         msg = 'Getting Bored. Motivation Message Required.'  
      if i == 3.0 and j == 3.0:
         msg = 'Affected with Multiple Problems. Motivation Message Required.'  
      if i == 3.0 and j == 4.0:
         msg = 'Getting Frustrated. Motivation Message Required.' 
      if i == 3.0 and j == 5.0:
         msg = 'Looking Confused. Motivation Message Required.' 

      if i == 4.0 and j == 0.0:
         msg = 'Weldone! You are performing well.'
      if i == 4.0 and j == 1.0:
         msg = 'Affected with Concentration. Motivation Message Required.'  
      if i == 4.0 and j == 2.0:
         msg = 'Getting Bored. Motivation Message Required.'  
      if i == 4.0 and j == 3.0:
         msg = 'Affected with Multiple Problems. Motivation Message Required.'  
      if i == 4.0 and j == 4.0:
         msg = 'Getting Frustrated. Motivation Message Required.' 
      if i == 4.0 and j == 5.0:
         msg = 'Looking Confused. Motivation Message Required.' 

      if i == 5.0 and j == 0.0:
         msg = 'Weldone! You are performing well.'
      if i == 5.0 and j == 1.0:
         msg = 'Affected with Concentration. Motivation Message Required.'  
      if i == 5.0 and j == 2.0:
         msg = 'Getting Bored. Motivation Message Required.'  
      if i == 5.0 and j == 3.0:
         msg = 'Affected with Multiple Problems. Motivation Message Required.'  
      if i == 5.0 and j == 4.0:
         msg = 'Getting Frustrated. Motivation Message Required.' 
      if i == 5.0 and j == 5.0:
         msg = 'Looking Confused. Motivation Message Required.' 

      context= {'data':msg}
      return render(request, 'AdminScreen.html', context)
    
