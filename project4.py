# Music Type Prediction Project
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

music_df = pd.read_csv('music.csv')
music_df.head()
X = music_df.drop(columns=['genre'])
y = music_df['genre']

model = DecisionTreeClassifier()
model.fit(X,y)

joblib.dump(model, 'music-recommender.joblib')

# predictions = model.predict([[21,1],[22,0]])
# predictions
