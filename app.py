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

# Load data for recommendation system
with open('movies_dict.pkl', 'rb') as file:
    movies_dict = pickle.load(file)
movies = pd.DataFrame(movies_dict)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# Configure Streamlit page
st.set_page_config(
    page_title="Entertainment Insights",
    page_icon="🎬",
    layout="wide"
)

# Navigation Bar
selected = option_menu(
    menu_title=None,
    options=["Movie Recommendations", "Actor and Movie Search"],
    icons=["film", "search"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "blue", "font-size": "25px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "3px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#2c3e50"},
    }
)

