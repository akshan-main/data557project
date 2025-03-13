import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data():
    file_path = "salary.txt"
    df = pd.read_csv(file_path, delim_whitespace=True)
    return df

df = load_data()

# Remove unnecessary columns from the variable filter
excluded_columns = ["case", "id", "sex", "year"]
available_variables = [col for col in df.columns if col not in excluded_columns]

# Streamlit Page Setup
st.set_page_config(page_title="About the Data", layout="wide")

# Title and description
st.title("About the Data")
st.write("This interactive page allows you to explore the faculty salary dataset.")

# Sidebar Filters
with st.sidebar:
    st.header("Filter Data")
    variable = st.selectbox("Select Variable", available_variables, index=available_variables.index("salary"))
    sex_filter = st.multiselect("Select Sex", df["sex"].unique(), default=df["sex"].unique())
    rank_filter = st.multiselect("Select Rank", df["rank"].dropna().unique(), default=df["rank"].dropna().unique())
    degree_filter = st.multiselect("Select Degree", df["deg"].unique(), default=df["deg"].unique())
    field_filter = st.multiselect("Select Field", df["field"].unique(), default=df["field"].unique())
    admin_filter = st.multiselect("Admin Role", df["admin"].unique(), default=df["admin"].unique())
    year_choice = st.selectbox("Select Year", sorted(df["year"].unique()), index=list(sorted(df["year"].unique())).index(95))
    yrdeg_range = st.slider("Select Year Degree Attained Range", int(df["yrdeg"].min()), int(df["yrdeg"].max()), (int(df["yrdeg"].min()), int(df["yrdeg"].max())))

# Variable Descriptions
st.subheader("Variable Names and Descriptions")
st.markdown("""
- **case** = Case number
- **id** = Identification number for the faculty member
- **sex** = M (male) or F (female)
- **deg** = Highest degree attained: PhD, Prof (professional degree, e.g., medicine or law), or Other (Master's or Bachelor's degree)
- **yrdeg** = Year highest degree attained
- **field** = Arts (Arts and Humanities), Prof (professional school, e.g., Business, Law, Engineering, or Public Affairs), or Other
- **startyr** = Year in which the faculty member was hired (2 digits)
- **year** = Year (2 digits)
- **rank** = Rank of the faculty member in this year: Assist (Assistant), Assoc (Associate), or Full (Full)
- **admin** = Indicator of whether the faculty member had administrative duties (e.g., department chair) in this year: 1 (yes), or 0 (no)
- **salary** = Monthly salary of the faculty member in this year in dollars
""")

# Apply Filters
df_filtered = df[(df["sex"].isin(sex_filter)) & 
                 (df["rank"].isin(rank_filter)) & 
                 (df["deg"].isin(degree_filter)) & 
                 (df["field"].isin(field_filter)) & 
                 (df["admin"].isin(admin_filter)) & 
                 (df["year"] == year_choice) & 
                 (df["yrdeg"].between(yrdeg_range[0], yrdeg_range[1]))]

# Ensure unique faculty members count properly
df_filtered_unique = df_filtered.drop_duplicates(subset=["id"])

# Compute additional statistics
num_unique_ids = df_filtered_unique["id"].nunique()
num_female = df_filtered_unique[df_filtered_unique["sex"] == "F"]["id"].nunique()
num_male = df_filtered_unique[df_filtered_unique["sex"] == "M"]["id"].nunique()
rank_counts = df_filtered_unique["rank"].value_counts().to_dict()
degree_counts = df_filtered_unique["deg"].value_counts().to_dict()
field_counts = df_filtered_unique["field"].value_counts(normalize=True).mul(100).round(1).to_dict()
admin_counts = df_filtered_unique["admin"].value_counts().to_dict()

# Display Data Overview
st.subheader("Data Overview")
st.write(f"Per chosen variables in **{year_choice}** year, the data contains **{num_unique_ids}** unique faculty members, with **{num_female}** females and **{num_male}** males.")
st.write(f"- **Rank Distribution:** {', '.join([f'{k}: {v}' for k, v in rank_counts.items()])}")
st.write(f"- **Degree Distribution:** {', '.join([f'{k}: {v}' for k, v in degree_counts.items()])}")
st.write(f"- **Field Distribution (%):** {', '.join([f'{k}: {v}%' for k, v in field_counts.items()])}")
st.write(f"- **Admin Role:** {', '.join([f'{k}: {v}' for k, v in admin_counts.items()])}")

# Rank Analysis
if variable == "rank":
    st.subheader("Rank Distribution by Sex")
    st.write(df_filtered.groupby("sex")["rank"].value_counts().unstack())
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="rank", hue="sex", data=df_filtered, palette="coolwarm")
    plt.title("Rank Distribution by Sex")
    st.pyplot(fig)
    
# Start Year Analysis
if variable == "startyr":
    st.subheader("Start Year Distribution by Sex")
    st.write(df_filtered.groupby("sex")["startyr"].describe())
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="sex", y="startyr", data=df_filtered, palette="coolwarm")
    plt.title("Start Year Distribution by Sex")
    st.pyplot(fig)

# Year Degree Attained Analysis
if variable == "yrdeg":
    st.subheader("Year Degree Attained Distribution by Sex")
    st.write(df_filtered.groupby("sex")["yrdeg"].describe())
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="sex", y="yrdeg", data=df_filtered, palette="coolwarm")
    plt.title("Year Degree Attained Distribution by Sex")
    st.pyplot(fig)

# Academic Field Analysis
if variable == "field":
    st.subheader("Academic Field Distribution by Sex")
    st.write(df_filtered.groupby("sex")["field"].value_counts().unstack())
    field_counts_df = df_filtered.groupby(["sex", "field"]).size().unstack().apply(lambda x: x / x.sum(), axis=1).mul(100).round(1)
    field_counts_df.plot(kind="bar", stacked=True, colormap="viridis")
    plt.title("Proportion of Fields by Sex (%)")
    plt.ylabel("Percentage")
    st.pyplot(plt)

# Degree Analysis
if variable == "deg":
    st.subheader("Degree Distribution by Sex")
    st.write(df_filtered.groupby("sex")["deg"].value_counts().unstack())
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="deg", hue="sex", data=df_filtered, palette="coolwarm")
    plt.title("Degree Distribution by Sex")
    st.pyplot(fig)

# Admin Role Analysis
if variable == "admin":
    st.subheader("Admin Role Distribution by Sex")
    st.write(df_filtered.groupby("sex")["admin"].value_counts().unstack())
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="admin", hue="sex", data=df_filtered, palette="coolwarm")
    plt.title("Admin Role Distribution by Sex")
    st.pyplot(fig)

# Salary Analysis
if variable == "salary":
    st.subheader("Salary Analysis")
    
    # Boxplot by Sex
    st.write("### Boxplot of Salary by Sex")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="sex", y="salary", data=df_filtered, palette="coolwarm")
    ax.set_title("Salary Distribution by Sex")
    st.pyplot(fig)
    
    # Summary Stats by Sex
    st.write("### Summary Statistics by Sex")
    st.write(df_filtered.groupby("sex")["salary"].describe())
    
    # Distribution of Salary by Sex
    st.write("### Salary Distribution by Sex")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df_filtered, x="salary", hue="sex", kde=True, bins=30, palette="coolwarm")
    ax.set_title("Salary Distribution by Sex")
    st.pyplot(fig)
