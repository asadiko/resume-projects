#This code will build a recommendation system using the scikit-learn library. 
# The ratings data is loaded into a pandas dataframe, and a pivot table is created. 
# The pivot table is then converted into a sparse matrix, which is used to train a NearestNeighbors model. 
# The function get_recommendations takes the trained model, the data, the movie index, 
# and the number of recommendations as input and returns the recommended movies for the given movie.
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Load the data into a pandas dataframe
df = pd.read_csv('ratings_data.csv')

# Create a pivot table
pivot_table = df.pivot_table(
    index='userId', columns='movieId', values='rating').fillna(0)

# Create a sparse matrix
matrix = pivot_table.values

# Create a NearestNeighbors model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(matrix)

# Define a function to get the recommendations


def get_recommendations(model, data, movie_idx, n_recommendations):
    distances, indices = model.kneighbors(
        data[movie_idx].reshape(1, -1), n_neighbors=n_recommendations+1)
    raw_recommends = sorted(
        list(zip(indices.squeeze(), distances.squeeze())), key=lambda x: x[1])[:0:-1]
    return pivot_table.iloc[i[0]].sort_values(ascending=False)


# Get recommendations for a given movie
movie_idx = 7
print(get_recommendations(model, matrix, movie_idx, 10))
