from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def home(request):
    return render (request, "home.html")
def interface(request):
    return render (request, "interface.html")
def explore(request):
    return render (request, "explore.html") 
def final(request):
    return render (request, 'final.html')
def result(request):
     
    data = pd.read_csv(r"C://Users//monis//Downloads//archive (1)//diabetes.csv")

    x = data.drop("Outcome", axis=1)
    y = data["Outcome"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    input_data = [[val1, val2, val3, val4, val5, val6, val7, val8]]

    pred = model.predict(input_data)

    result1 = ""
    if pred == 1:
        result1 = "POSITIVE"
    else:
        result1 = "NEGATIVE"
    return render(request, 'result.html', {'result2': result1})

