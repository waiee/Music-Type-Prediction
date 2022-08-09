# Music Type Prediction Project
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib as jb

#--- DATAFRAME ---
music_df = pd.read_csv('music.csv')
music_df.head()
X = music_df.drop(columns=['genre'])
y = music_df['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#--- DECISION TREE MODEL---
model = DecisionTreeClassifier()

# --- TRAIN MODEL ---
model.fit(X,y)

#--- MODEL PERSISTANCE ---
# jb.dump(model, 'music-recommender.joblib')
# model = jb.load('music-recommender.joblib')

predictions = model.predict(X_test)


# predictions = model.predict([[21,1], [22, 0]])
predictions

# predictions = model.predict([[21,1],[22,0]])
# predictions
