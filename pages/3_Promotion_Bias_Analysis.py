import streamlit as st
from hypothesis_tests import *
from data_loader import load_data

df = load_data()

st.title("Promotion Bias Analysis")


# Create text input fields for year selection (on the same line)
col1, col2 = st.columns(2)

with col1:
    y1 = st.sidebar.text_input("Enter Start Year (≥ 80):", value="80")
with col2:
    y2 = st.sidebar.text_input("Enter End Year (≤ 95):", value="95")
st.header(f"Exploring Bias in Granting Salary Increases from : 19{y1}-{y2}")
# Validate inputs
try:
    y1, y2 = int(y1), int(y2)

    if y1 < 80 or y2 > 95 or y1 >= y2:
        st.error("Please enter valid years: Start Year must be ≥ 80, End Year must be ≤ 95, and Start Year < End Year.")
    else:
        # Perform hypothesis test
        t_stat, p_value, std_error, male_salaries, female_salaries = tTestSalaryIncrease(df, yrStart=y1, yrEnd=y2)

        st.pyplot(plot_salary_kde(male_salaries, female_salaries, std_error, t_stat, p_value, kind="Salary Increase per Year"))

except ValueError:
    st.error("Please enter valid numeric values for the years.")


t_stat, p_val1, se1, z_stat, p_val2, data_p, data_np, male_promotion_time, female_promotion_time, p1, n1, p2, n2, p = promotionStats(df, curr_rank = 'Full', prev_rank = 'Assoc', percentile = 0.50)
st.header("Exploring Bias in Promotion Time")
st.pyplot(plot_salary_kde(male_promotion_time, female_promotion_time, se1, t_stat, p_val1, kind="Promotion Time (Years)"))


st.header("Exploring Bias in Proportion Promoted")
prop_male_promoted = p1
prop_female_promoted = p2
pooled_proportion = p
z_stat = z_stat
p_value = p_val2
reject_null = p_value < 0.05

decision_text = "Reject Null Hypothesis" if reject_null else "No Reason to Reject \nNull Hypothesis"
decision_color = "red" if reject_null else "green"

# st.subheader("Promotion Proportions by Gender")

fig, ax = plt.subplots(figsize=(6, 4))

labels = ["Male", "Female"]
values = [prop_male_promoted, prop_female_promoted]

ax.bar(labels, values, color=["blue", "purple"], alpha=0.6)
ax.axhline(y=pooled_proportion, color="red", linestyle="dashed", label=f"Pooled Proportion: {pooled_proportion:.3f}")

for i, v in enumerate(values):
    ax.text(i, v + 0.01, f"{v:.3%}", ha='center', fontsize=12, fontweight="bold")

ax.set_ylim(0, 1)
ax.set_ylabel("Proportion Promoted")
ax.set_title("Proportion of Promotions by Gender")
ax.legend()


p_val_string = f"Z-value: {z_stat:.2f}\nP-value: {p_value:.4f}" if p_value>0.001 else f"Z-value: {z_stat:.2f}\nP-value < 0.001"
plt.text(
    0.60, 0.85,
    p_val_string,
    transform=plt.gca().transAxes,
    fontsize=9, fontweight="bold", color="black",
    verticalalignment='top', horizontalalignment='left'
)

plt.text(
    0.60, 0.75,
    decision_text,
    transform=plt.gca().transAxes,
    fontsize=10, fontweight="bold", color=decision_color,
    verticalalignment='top', horizontalalignment='left'
    )

st.pyplot(fig)