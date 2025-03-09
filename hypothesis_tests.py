import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm
import numpy as np

def tTestYear(df, year=95, starting=False):
    data_yr = df[df['year'] == df['startyr']] if starting == True else df[df['year'] == year]

    male_salaries = data_yr[data_yr['sex'] == 'M']['salary']
    female_salaries = data_yr[data_yr['sex'] == 'F']['salary']

    t_stat, p_value = ttest_ind(male_salaries, female_salaries, equal_var=False)

    n_m, n_f = len(male_salaries), len(female_salaries)
    var_m, var_f = np.var(male_salaries, ddof=1), np.var(female_salaries, ddof=1)
    std_error = np.sqrt((var_m / n_m) + (var_f / n_f))
    
    return t_stat, p_value, std_error

def tTestSalaryIncrease(df):
    data = df[(df['year'] >= 90) & (df['year'] <= 95)]
    data = data.sort_values(by=['id', 'year'])
    # data['salary_increase'] = data.groupby('id')['salary'].diff().fillna(0)

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
    
    return t_stat, p_value, std_error

def promotion_time_test(data):
    data['promotion_time'] = data['rank_end_yr'] - data['rank_start_yr'] + 1

    male_promotion_time = data[data.sex == 'M'].promotion_time
    female_promotion_time = data[data.sex == 'F'].promotion_time

    t_stat, p_value = ttest_ind(male_promotion_time, female_promotion_time, equal_var=False)
  
    return t_stat, p_value

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
    z_stat_q4_2, p_value_q4_2 = sm.stats.proportions_ztest([p1, p2], [n1, n2], alternative='two-sided')
    
    return z_stat_q4_2, p_value_q4_2

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

    t_stat, p_val1 = promotion_time_test(data_p)
    z_stat, p_val2 = promotion_proportion_test(data_p, data_np, percentile)
    return t_stat, p_val1, z_stat, p_val2, data_p, data_np