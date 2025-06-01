import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import google.generativeai as genai

# Configure Google Generative AI
API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Function to search for actors or movies
def search_actor_or_movie(input_text, search_type):
    if search_type == "Actor":
        prompt = (
            f"Provide details for actor '{input_text}':\n"
            f"- Name\n- Birthdate\n- Movies worked in"
        )
    else:
        prompt = (
            f"Provide details for the movie '{input_text}':\n"
            f"- Name\n- Release date\n- Director\n- Genre/Theme\n- Actors involved\n"
            f"- Short description"
        )
    response = model.generate_content(prompt)
    return response.text

