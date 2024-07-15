from flask import *
import pandas as pd
from sklearn.linear_model import LogisticRegression

app=Flask(__name__)
####################################
url = "https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/wines/winequality-red.csv" 
wine= pd.read_csv(url, sep=';') 

wine.isnull().sum()

X = wine[['fixed acidity','volatile acidity','citric acid',	'residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']]
Y=wine['quality']

modelwine = LogisticRegression()
modelwine.fit(X,Y)
res=modelwine.predict([[ 4.6,0.12,0.0,0.9,0.012,1.0,6.0,0.99007,2.74,0.33,8.4]]) 
op=res
###################################

@app.route('/')
def hello_world():
  return render_template("index.html")  

@app.route('/project')
def project():
  return render_template("form.html") 
 
@app.route('/predict',methods=['POST'])
def predict():
  fixedacidity=float(request.form['fixedacidity'])
  volatileacidity=float(request.form['volatileacidity'])
  citricacid=float(request.form['citricacid'])
  residualsugar=float(request.form['residualsugar'])
  chlorides=float(request.form['chlorides'])
  freesulfurdioxide=float(request.form['freesulfurdioxide'])
  totalsulfurdioxide=float(request.form['totalsulfurdioxide'])
  density=float(request.form['density'])
  pH=float(request.form['pH'])
  sulphates=float(request.form['sulphates'])
  alcohol=float(request.form['alcohol'])
  
  res=modelwine.predict([[fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol]])
  
  if res >= 7:
        result="PREDICTED RESULT :"+" HIGH QUALITY WINE."
  elif res >= 5:
        result="PREDICTED RESULT :"+" MEDIUM QUALITY WINE."
  else:
        result="PREDICTED RESULT :"+" LOW QUALITY WINE."
      
  return render_template("form.html",result=result) 
  
@app.route('/home')
def home():
  return render_template("index.html")

if __name__=='__main__':
  app.run(debug=True)              