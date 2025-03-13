import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import statsmodels.api as sm



st.title("Academic Salary Prediction")
st.markdown("""
This page predicts **academic salaries** over time using a regression model trained on historical data.  
Use side of the page to adjust inputs. 
""")

@st.cache_resource
def load_and_train_model():
    df = pd.read_csv('salary.txt', delim_whitespace=True)
    df = df.dropna(subset=['rank'])

    df['year_full'] = df['year'] + 1900
    df['startyr_full'] = df['startyr'] + 1900
    df['yrdeg_full'] = df['yrdeg'] + 1900
    df['experience'] = np.maximum(df['year_full'] - df['startyr_full'], 0)

    categorical_features = ['sex', 'deg', 'field', 'rank']
    numeric_features = ['yrdeg_full', 'year_full', 'experience', 'admin']
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_features),
        ('num', 'passthrough', numeric_features)
    ])

    model_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Train Model
    X = df[categorical_features + numeric_features]
    y = df['salary']
    model_pipeline.fit(X, y)

    return model_pipeline, df, X, y

# Loading Model and Dataset
model, df, X, y = load_and_train_model()

# Input Form
with st.sidebar.form("salary_prediction_form"):
    st.header("Input Parameters")
    degree = st.selectbox("Highest Degree", df["deg"].unique().tolist(), key="degree")
    year_of_degree = st.number_input("Year of Degree", min_value=int(df["yrdeg_full"].min()), max_value=int(df["yrdeg_full"].max()), value=int(df["yrdeg_full"].max()), format="%d", key="year_of_degree")

    start_year = st.slider("Start Year", min_value=year_of_degree, max_value=2020, value=year_of_degree, key="start_year")

    field = st.selectbox("Field of Study", df["field"].unique().tolist(), key="field")
    rank = st.selectbox("Current Academic Rank", df["rank"].unique().tolist(), key="rank")
    years_in_rank = st.number_input("Years in Current Rank", min_value=0, max_value=50, value=0, key="years_in_rank")
    admin_role = st.checkbox("Has Administrative Role?", value=False, key="admin_role")
    admin = 1 if admin_role else 0
    prediction_year = st.number_input("Enter the Year for Salary Prediction", min_value=start_year, max_value=start_year + 20, value=start_year + 5, key="prediction_year")  # Replaced dropdown
    submit_button = st.form_submit_button("Submit")

if submit_button:
    pred_input_rows = []
    current_rank = rank
    current_years_in_rank = years_in_rank

    years_range = list(range(start_year, start_year + 20))

    for yr in years_range:
        exp = yr - start_year
        
        if current_years_in_rank >= 6:
            if current_rank == "Assist":
                current_rank = "Assoc"
                current_years_in_rank = 0
            elif current_rank == "Assoc":
                current_rank = "Full"
                current_years_in_rank = 0

        current_years_in_rank += 1

        pred_input_rows.append({
            "sex": "F", "deg": degree, "field": field, "rank": current_rank,
            "admin": admin, "year_full": yr, "yrdeg_full": year_of_degree, "startyr_full": start_year, "experience": exp
        })
        pred_input_rows.append({
            "sex": "M", "deg": degree, "field": field, "rank": current_rank,
            "admin": admin, "year_full": yr, "yrdeg_full": year_of_degree, "startyr_full": start_year, "experience": exp
        })

    pred_input_df = pd.DataFrame(pred_input_rows)
    pred_salaries = model.predict(pred_input_df)
    pred_salaries = np.clip(pred_salaries, a_min=1200, a_max=90000)
    pred_input_df['Predicted Salary'] = pred_salaries
    plot_df = pred_input_df.copy()
    plot_df['Sex'] = plot_df['sex'].map({"F": "Female", "M": "Male"})
    plot_df = plot_df[['year_full', 'Sex', 'Predicted Salary']].rename(columns={'year_full': 'Year'})
    plot_df['Year'] = plot_df['Year'].astype(str)  # Convert to string for display

    color_scale = alt.Scale(
        domain=["Female", "Male"],
        range=["pink", "blue"]
    )

    chart = alt.Chart(plot_df).mark_line().encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('Predicted Salary:Q', title='Predicted Salary', scale=alt.Scale(domain=[0, 20000])),
        color=alt.Color('Sex:N', title='Sex', scale=color_scale),
        tooltip=['Year', 'Sex', 'Predicted Salary']
    ).properties(title='Predicted Salary Trend by Sex').interactive()

    st.altair_chart(chart, use_container_width=True)

    # Salary
    female_salary = pred_input_df[(pred_input_df['year_full'] == prediction_year) & (pred_input_df['sex'] == 'F')]['Predicted Salary']
    male_salary = pred_input_df[(pred_input_df['year_full'] == prediction_year) & (pred_input_df['sex'] == 'M')]['Predicted Salary']

    st.write(f"### **Predicted Salary in {prediction_year}**")
    st.write(f"**Female:** ${female_salary.values[0]:,.0f}" if not female_salary.empty else "No data available")
    st.write(f"**Male:** ${male_salary.values[0]:,.0f}" if not male_salary.empty else "No data available")

# Model Coefficients
X_transformed = model.named_steps["preprocessor"].transform(X)
X_transformed = sm.add_constant(X_transformed)
sm_model = sm.OLS(y, X_transformed).fit()

beta_labels = [f"β{i}" for i in range(len(sm_model.params))]
coef_df = pd.DataFrame({
    "β Coefficients": beta_labels,  
    "Feature": ["Intercept "] + list(model.named_steps["preprocessor"].get_feature_names_out()),
    "Coefficient": sm_model.params,
    "P-Value": sm_model.pvalues,
    "Lower 95% CI": sm_model.conf_int()[0],
    "Upper 95% CI": sm_model.conf_int()[1]
})

coef_df["P-Value"] = coef_df["P-Value"].apply(lambda x: "0.00" if x == 0 else (f"{x:.2e}" if x < 0.0001 else round(x, 4)))

st.markdown("### Regression Coefficients & Statistical Values")
st.dataframe(coef_df)
