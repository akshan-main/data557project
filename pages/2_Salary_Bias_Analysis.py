import streamlit as st
import pandas as pd
from hypothesis_tests import *
from data_loader import load_data


st.title("Salary Bias Analysis")
df = load_data()

year = st.sidebar.number_input("Enter Year", min_value=76, max_value=95, value=95)
st.header(f"Exploring Bais in Salary for the Year : 19{year}")
t_stat, p_value, se1 = tTestYear(df, year=year)
male_salaries_yr = df[(df["sex"] == "M") & (df["year"] == year)]["salary"]
female_salaries_yr = df[(df["sex"] == "F") & (df["year"] == year)]["salary"]
st.pyplot(plot_salary_kde(male_salaries_yr, female_salaries_yr, se1, t_stat, p_value,  kind="Salary"))

st.header("Exploring Bias in Starting Salary")
t_stat, p_value, se2 = tTestYear(df, starting=True)
male_salaries = df[df["sex"] == "M"]["salary"]
female_salaries = df[df["sex"] == "F"]["salary"]
st.pyplot(plot_salary_kde(male_salaries, female_salaries, se2, t_stat, p_value, kind="Salary"))