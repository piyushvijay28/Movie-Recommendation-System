import streamlit as st
import pickle
import pandas as pd
import zipfile
import os



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]
        #fecth poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies




# Specify the path to your zip folder and the name of the pkl file inside it
zip_folder_path = 'similarity.zip'
pkl_filename = 'similarity.pkl'

    # Open the zip file
with zipfile.ZipFile(zip_folder_path, 'r') as zip_ref:
        # Check if the pkl file exists in the zip folder
    if pkl_filename in zip_ref.namelist():
            # Extract the pkl file to a temporary directory (current directory in this case)
        zip_ref.extract(pkl_filename, './')

            # Load the pkl file
        with open(pkl_filename, 'rb') as f:
            similarity = pickle.load(f)

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)



st.title('Movie Recommender System')

Selected_movie_name=st.selectbox('Search Movie name',movies['title'].values)

if st.button('Recommend'):
    recommendation=recommend(Selected_movie_name)
    for i in recommendation:
     st.write(i)
