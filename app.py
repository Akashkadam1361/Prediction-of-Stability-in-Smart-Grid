import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style='whitegrid')
data =pd.read_csv('smart_grid_stability.csv')
abalone_data = data.replace({"stabf": {"unstable":0,"stable":1,}})
abalone_data.info()
stab_features = abalone_data.drop(['stab','stabf'],axis=1)
stab_labels =abalone_data['stabf'].copy()
from sklearn.preprocessing import MinMaxScaler
X = stab_features
mm = MinMaxScaler()
X_normalized = mm.fit_transform(X)
from sklearn.preprocessing import add_dummy_feature
x_new = add_dummy_feature(X_normalized)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_new, stab_labels, test_size = 0.2)
from sklearn.ensemble import RandomForestClassifier
rfn= RandomForestClassifier(n_estimators=70, oob_score=True, n_jobs=-1, random_state=101, max_features=None, min_samples_leaf = 30)
classifier= rfn.fit(X_train,y_train) 
y_pred = rfn.predict(X_test)
