# Music Type Prediction Project
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib as jb

# music_df = pd.read_csv('music.csv')
# music_df.head()
# X = music_df.drop(columns=['genre'])
# y = music_df['genre']

#--- DECISION TREE MODEL---
# model = DecisionTreeClassifier()

# --- TRAIN MODEL ---
# model.fit(X,y)

#--- MODEL PERSISTANCE ---
# jb.dump(model, 'music-recommender.joblib')
model = jb.load('music-recommender.joblib')
predictions = model.predict([[21,1]])
predictions

# predictions = model.predict([[21,1],[22,0]])
# predictions
