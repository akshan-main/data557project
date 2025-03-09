import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from data_loader import load_data

df = load_data()
st.title("About the Data")

# Function to create proportion plots
def plot(feature, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    # Compute proportions
    prop_df = df.groupby(["sex", feature]).size().unstack().fillna(0)
    prop_df = prop_df.div(prop_df.sum(axis=1), axis=0) * 100  # Convert to percentage

    # Plot stacked bar chart
    prop_df.T.plot(kind="bar", stacked=True, colormap="coolwarm", ax=ax, width=0.6)
    ax.set_ylabel("Percentage (%)")
    ax.set_title(title)
    ax.legend(title="Sex", labels=["Male", "Female"])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Keep labels horizontal

    return fig

def plot_proportion(feature, title):
    unique_df = df.drop_duplicates(subset='id')
    counts = unique_df.groupby('sex')[feature].value_counts().unstack()
    proportions = counts.div(counts.sum(axis=1), axis=0)

    fig, ax = plt.subplots(figsize=(10, 6))
    proportions.plot(kind='bar', stacked=True, ax=ax)

    ax.set_xticklabels(["Female", "Male"], rotation=0)
    for container in ax.containers:
        for bar in container:
            height = bar.get_height()
            if height > 0:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_y() + height / 2,
                    f"{height:.1%}",
                    ha='center', va='center', fontsize=10, color='black'
                )

    ax.set_xlabel("Sex")
    ax.set_ylabel("Proportion")
    ax.set_title(title)
    ax.legend(title=feature, bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_ylim(0, 1)

    return fig

# Define 2-row × 3-column grid layout
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# Generate and place charts in the grid
with col1:
    st.pyplot(plot_proportion("deg", "Degree Distribution"))

with col2:
    st.pyplot(plot_proportion("field", "Field Distribution"))

with col3:
    st.pyplot(plot_proportion("rank", "Rank Distribution"))

with col4:
    st.pyplot(plot_proportion("admin", "Admin Duties"))

with col5:
    st.pyplot(plot("pre_emp_gap", "Employment Gap Before Joining"))

with col6:
    st.pyplot(plot("promotion_time", "Promotion Time"))