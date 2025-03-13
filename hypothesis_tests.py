import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def tTestYear(df, year=95, starting=False):
    data_yr = df[df['year'] == df['startyr']] if starting == True else df[df['year'] == year]

    male_salaries = data_yr[data_yr['sex'] == 'M']['salary']
    female_salaries = data_yr[data_yr['sex'] == 'F']['salary']

    t_stat, p_value = ttest_ind(male_salaries, female_salaries, equal_var=False)

    n_m, n_f = len(male_salaries), len(female_salaries)
    var_m, var_f = np.var(male_salaries, ddof=1), np.var(female_salaries, ddof=1)
    std_error = np.sqrt((var_m / n_m) + (var_f / n_f))
    
    return t_stat, p_value, std_error

def tTestSalaryIncrease(df, yrStart, yrEnd):
    data = df[(df['year'] >= yrStart) & (df['year'] <= yrEnd)]
    data = data.sort_values(by=['id', 'year'])

    diff_func = lambda x: x.values[-1] - x.values[0]
    data = data.groupby('id')[['sex', 'year', 'salary']].agg({'sex': 'first', 'year': diff_func, 'salary': diff_func}).reset_index()
    data = data.rename(columns={'year': 'year_diff', 'salary': 'salary_diff'})
    data = data[data.year_diff > 0]
    data['salary_increase_slope'] = data.salary_diff / data.year_diff

    male_salaries = data[data['sex'] == 'M']['salary_increase_slope']
    female_salaries = data[data['sex'] == 'F']['salary_increase_slope']
    t_stat, p_value = ttest_ind(male_salaries, female_salaries, equal_var=False)

    n_m, n_f = len(male_salaries), len(female_salaries)
    var_m, var_f = np.var(male_salaries, ddof=1), np.var(female_salaries, ddof=1)
    std_error = np.sqrt((var_m / n_m) + (var_f / n_f))
    
    female_salaries = data[data['sex'] == 'F']['salary_increase_slope']
    return t_stat, p_value, std_error, male_salaries, female_salaries

def promotion_time_test(data):
    data['promotion_time'] = data['rank_end_yr'] - data['rank_start_yr'] + 1

    male_promotion_time = data[data.sex == 'M'].promotion_time
    female_promotion_time = data[data.sex == 'F'].promotion_time

    t_stat, p_value = ttest_ind(male_promotion_time, female_promotion_time, equal_var=False)

    n_m, n_f = len(male_promotion_time), len(female_promotion_time)
    var_m, var_f = np.var(male_promotion_time, ddof=1), np.var(female_promotion_time, ddof=1)
    std_error = np.sqrt((var_m / n_m) + (var_f / n_f))
  
    return t_stat, p_value, std_error,  male_promotion_time, female_promotion_time

def promotion_proportion_test(data_p, data_np, percentile = 0.50):
    promotion_time = data_p['promotion_time'].quantile(percentile)
    data_np_1 = data_np[data_np['curr_rank_time'] >= promotion_time]

    promoted_males = data_p[data_p.sex == 'M'].shape[0]
    non_promoted_males = data_np_1[data_np_1.sex == 'M'].shape[0]
    total_males = promoted_males + non_promoted_males

    promoted_females = data_p[data_p.sex == 'F'].shape[0]
    non_promomted_females = data_np_1[data_np_1.sex == 'F'].shape[0]
    total_females = promoted_females + non_promomted_females

    p1 = promoted_males / total_males
    p2 = promoted_females / total_females
    n1 = total_males
    n2 = total_females
    p = (promoted_males + promoted_females) / (n1+n2)
    z_stat_q4_2, p_value_q4_2 = sm.stats.proportions_ztest([p1, p2], [n1, n2], alternative='two-sided')
    
    return z_stat_q4_2, p_value_q4_2, p1, n1, p2, n2, p

def promotionStats(df, curr_rank = 'Full', prev_rank = 'Assoc', percentile = 0.50):
    if curr_rank not in ['Full', 'Assoc'] or prev_rank not in ['Assist', 'Assoc']:
        raise ValueError("Invalid input. Please enter valid ranks.")
    
    promoted_ids = set(df[df['rank'] == prev_rank]['id'].values).intersection(set(df[df['rank'] == curr_rank]['id'].values))
    non_promoted_ids = set(df[df['rank'] == prev_rank]['id'].values).difference(promoted_ids)

    data = df[df['rank'] == prev_rank]
    data = data.sort_values(by=['id', 'year'])
    data['rank_start_yr'] = data.groupby(['id', 'rank'])['year'].transform('min')
    data['rank_end_yr'] = data.groupby(['id', 'rank'])['year'].transform('max')
    data['curr_rank_time'] = data['rank_end_yr'] - data['rank_start_yr'] + 1

    data_p = data[data['id'].isin(promoted_ids)]
    data_np = data[data['id'].isin(non_promoted_ids)]

    # Gender distribution
    print("Promoted Sample - Gender Distribution: ")
    print(data_p.groupby('sex').agg({'id': 'nunique'}))
    print("Promoted - Non-Promoted Sample - Gender Distribution: ")
    print(pd.concat([data_p,data_np]).groupby('sex').agg({'id': 'nunique'}))

    t_stat, p_val1,se1,  male_promotion_time, female_promotion_time = promotion_time_test(data_p)
    z_stat, p_val2, p1, n1, p2, n2, p = promotion_proportion_test(data_p, data_np, percentile)
    return t_stat, p_val1, se1, z_stat, p_val2, data_p, data_np, male_promotion_time, female_promotion_time, p1, n1, p2, n2, p

def plot_salary_kde(male_salaries, female_salaries, std_error, t_stat, p_value, kind):
    plt.figure(figsize=(10, 6))

    sns.kdeplot(male_salaries, fill=True, color="blue", alpha=0.5, label=f"Density of Male {kind}")
    sns.kdeplot(female_salaries, fill=True, color="purple", alpha=0.5, label=f"Density of Female {kind}")

    mean_male, mean_female = male_salaries.mean(), female_salaries.mean()
    mean_diff = abs(mean_male - mean_female)
    mean_se_ratio = mean_diff / std_error

    plt.axvline(mean_male, color="blue", linestyle="dashed", label=f"Mean of Male {kind}: ${mean_male:,.0f}")
    plt.axvline(mean_female, color="purple", linestyle="dashed", label=f"Mean of Female {kind}: ${mean_female:,.0f}")

    reject_null = p_value < 0.05
    decision_text = "Reject Null Hypothesis" if reject_null else "No Reason to Reject \nNull Hypothesis"
    decision_color = "red" if reject_null else "green"

    
    plt.xlabel("Salary ($)")
    plt.ylabel("Density")
    plt.title(f"Overall {kind} Distribution")
    plt.legend()

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