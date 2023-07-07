
import pandas as pd
import numpy as np

df = pd.read_csv('D:/SEM 4/ES PROJECT/Web/rainfall in india 1901-2015.csv')
df
SUBDIVISION_N=int(input("SUBDIVISION_N:"))
YEAR=int(input("YEAR:"))
Jan_Feb=int(input("Jan-Feb:"))
Mar_May=int(input("Mar-May:"))
Jun_Sep=int(input("Jun-Sep"))
Oct_Dec=int(input("Oct-Dec:"))

#string to numericals
from sklearn.preprocessing import LabelEncoder
Numerics = LabelEncoder()
df['SUBDIVISION_N'] = Numerics.fit_transform(df['SUBDIVISION'])
df = df.drop(['SUBDIVISION'],axis =1)
df

from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_df = pd.DataFrame(my_imputer.fit_transform(df))

# Imputation removed column names; put them back
imputed_df.columns = df.columns
df = imputed_df
df.isnull().sum()

y = df.ANNUAL
y = y.values.reshape(-1,1)

day_index = 2004
days = [i for i in range(y.size)]

df_features  = ['SUBDIVISION_N','YEAR','Jan-Feb','Mar-May','Jun-Sep','Oct-Dec']
#df_features  = ['SUBDIVISION_N','YEAR']
X = df[df_features]

from sklearn.model_selection import train_test_split

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)


inp = np.array([[SUBDIVISION_N],[YEAR],[Jan_Feb],[Mar_May],[Jun_Sep],[Oct_Dec]])
inp = inp.reshape(1,-1)



from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

model1 = LinearRegression()
model1.fit(X_train,y_train)
preds = model1.predict(X_valid)
preds
print(mean_absolute_error(y_valid,preds))
import sklearn.metrics as sm
#print("Mean absolute error =", round(sm.mean_absolute_error(y_valid, preds), 2))
#print("Mean squared error =", round(sm.mean_squared_error(y_valid, preds), 2))
print("R2 score =", round(sm.r2_score(y_valid,preds), 2))
print(model1.predict(inp))
