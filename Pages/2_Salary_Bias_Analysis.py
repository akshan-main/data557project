import streamlit as st
import pandas as pd
from hypothesis_tests import *
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data

def plot_salary_kde(male_salaries, female_salaries, std_error, t_stat, p_value):
    plt.figure(figsize=(10, 6))

    sns.kdeplot(male_salaries, fill=True, color="blue", alpha=0.5, label="Male Salary Density")
    sns.kdeplot(female_salaries, fill=True, color="purple", alpha=0.5, label="Female Salary Density")

    mean_male, mean_female = male_salaries.mean(), female_salaries.mean()
    mean_diff = abs(mean_male - mean_female)
    mean_se_ratio = mean_diff / std_error

    plt.axvline(mean_male, color="blue", linestyle="dashed", label=f"Male Salary Mean: ${mean_male:,.0f}")
    plt.axvline(mean_female, color="purple", linestyle="dashed", label=f"Female Salary Mean: ${mean_female:,.0f}")

    reject_null = p_value < 0.05
    decision_text = "Reject Null Hypothesis" if reject_null else "No Reason to Reject \nNull Hypothesis"
    decision_color = "red" if reject_null else "green"

    
    plt.xlabel("Salary ($)")
    plt.ylabel("Density")
    plt.title("Overall Salary Distribution")
    plt.xlim(0,14000)
    legend = plt.legend()

    plt.text(
    0.67, 0.77,
    f"Std Error: {std_error:.2f}\n"
    f"Difference in Means: {mean_se_ratio:.2f} × SE",
    transform=plt.gca().transAxes,
    fontsize=10, color="black",
    verticalalignment='top', horizontalalignment='left'
    )

    plt.text(
    0.67, 0.68,
    f"T-value: {t_stat:.2f}\nP-value: {p_value:.4f}",
    transform=plt.gca().transAxes,
    fontsize=12, fontweight="bold", color="black",
    verticalalignment='top', horizontalalignment='left'
)

    plt.text(
        0.67, 0.58,
        decision_text,
        transform=plt.gca().transAxes,
        fontsize=12, fontweight="bold", color=decision_color,
        verticalalignment='top', horizontalalignment='left'
    )

    return plt.gcf()

df = load_data()
st.title("Salary Bias Analysis")
st.header("Starting Salary")
t_stat, p_value, se = tTestYear(df, starting=True)
male_salaries = df[df["sex"] == "M"]["salary"]
female_salaries = df[df["sex"] == "F"]["salary"]
st.pyplot(plot_salary_kde(male_salaries, female_salaries, se, t_stat, p_value))

st.header("Salary for a Given Year")
year = st.number_input("Enter Year", min_value=00, max_value=95, value=95)
t_stat, p_value, se = tTestYear(df, year=year)
male_salaries_yr = df[(df["sex"] == "M") & (df["year"] == year)]["salary"]
female_salaries_yr = df[(df["sex"] == "F") & (df["year"] == year)]["salary"]
st.pyplot(plot_salary_kde(male_salaries_yr, female_salaries_yr, se, t_stat, p_value))