# Music Type Prediction Project
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_df = pd.read_csv('music.csv')
music_df.head()
