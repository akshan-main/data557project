import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from hypothesis_tests import *
import matplotlib.pyplot as plt

st.set_page_config(page_title="Salary Bias Analysis", layout="wide")

st.title("Exploring Differences between Male & Female Faculty at a US University")
st.header("Welcome! Use the sidebar to navigate all sections.")

st.header("Acknowledgements")
st.write("The dataset and questions were provided by Professor Scott Emerson.")
st.write("This project is made as deliverable for course DATA 557: Applied Statistics & Experimental Design, University of Washington.")

st.header("Background")
st.write( """  
Salary disparities between men and women in U.S. colleges and universities have been widely studied. While discrimination based on sex is illegal, other factors may contribute to these differences, such as experience, educational qualifications, academic field, administrative roles, and productivity.\n  
Faculty salaries are influenced by multiple factors, some of which may be intertwined with gender differences. Certain disciplines command higher salaries due to market demand. Experience and promotions also play a crucial role—salaries typically increase as faculty members advance in rank. Universities enforce strict timelines for promotion from Assistant to Associate Professor, usually within six years. However, there is no set timeline for promotion from Associate to full Professor. Additionally, faculty productivity, including research grants, publications, teaching performance, and administrative responsibilities, can impact salary levels.\n  
This project aims to analyze faculty salary data to determine whether there are statistically significant differences in average salaries between male and female faculty members within an institution.
""")


st.header("The Team:")
team_members = [
    {"name": "Aaditya Chopra", "photo": "./assets/profilepics/Profile.png", "linkedin": "https://www.linkedin.com/in/smeet-dedhia-9b430621b/"},
    {"name": "Akshan Krithick", "photo": "./assets/profilepics/Profile.png", "linkedin": "https://www.linkedin.com/in/smeet-dedhia-9b430621b/"},
    {"name": "Ayush Mall", "photo": "./assets/profilepics/Profile.png", "linkedin": "https://www.linkedin.com/in/smeet-dedhia-9b430621b/"},
    {"name": "Riddhesh Sawant", "photo": "./assets/profilepics/Profile.png", "linkedin": "https://www.linkedin.com/in/smeet-dedhia-9b430621b/"},
    {"name": "Smeet Dedhia", "photo": "./assets/profilepics/Smeet.png", "linkedin": "https://www.linkedin.com/in/smeet-dedhia-9b430621b/"},
    {"name": "Zhansaya Ussembayeva", "photo": "./assets/profilepics/Profile.png", "linkedin": "https://www.linkedin.com/in/smeet-dedhia-9b430621b/"},
]

cols = st.columns(3)

for i, member in enumerate(team_members):
    with cols[i % 3]:  # Arrange in 3 columns
        st.image(member["photo"], width=150)
        st.markdown(f"**{member['name']}**")
        st.markdown(f"[LinkedIn]({member['linkedin']})")


import streamlit as st
import os

st.sidebar.title("Debug Mode")

# Show current working directory
st.sidebar.write("Current directory:", os.getcwd())

# List all files in the current directory
st.sidebar.write("Files in directory:", os.listdir(os.getcwd()))

# Check if `pages/` exists
pages_path = os.path.join(os.getcwd(), "pages")
if os.path.exists(pages_path):
    st.sidebar.write("✅ `pages/` folder found!")
    st.sidebar.write("Files in `pages/`:", os.listdir(pages_path))
else:
    st.sidebar.write("❌ `pages/` folder NOT found! Please check deployment.")
