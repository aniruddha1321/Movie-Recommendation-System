import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import google.generativeai as genai

# Configure Google Generative AI
API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")