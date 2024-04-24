import pandas as pd
f=pd.read_csv("Iris.csv")
f.tail(5)
from sklearn.naive_bayes import GaussianNB as g
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tt
l=le()
f['Species']=l.fit_transform(f['Species'])
x=f.iloc[:,:5]
y=f.iloc[:,5]
print(x)
print(y)
xtr,xte,ytr,yte=tt(x,y,test_size=0.3)
gg=g()
gg.fit(xtr,ytr)
y_pred=gg.predict(xte)
from sklearn.metrics import accuracy_score
print(accuracy_score(yte,y_pred)*100)
