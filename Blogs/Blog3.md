# Exploring Gender Bias in University Promotions: A Data-Driven Analysis

Analyzing gender bias in university promotions using historical data (1980-1995). While promotion timelines appear similar for men and women, salary increases show a significant disparity. Data-driven insights highlight the need for fairer salary policies in academia.

---

## **Introduction**

Discussions around gender bias in workplace promotions are nothing new, and universities are no exception. To explore whether men and women experience differences in promotion time and salary increases in academia, we analyzed **promotion data from 1980 to 1995**.

To make the study fair and avoid skewed results, we **excluded faculty members who had been in their current roles for less than 7 years**, as that was the **median promotion time** across genders. This helped ensure that no one was unfairly included just because they had recently been promoted.

We focused on two key questions:
1. **Are salary increases different for male and female faculty?**
2. **Do men and women take different amounts of time to get promoted?**

## **Salary Increases: Evidence of Bias**

To check if men and women received different salary increments per year, we conducted a **t-test** comparing their yearly salary increases.

- Male faculty received an average salary increase of \$260 per year, while female faculty received \$210 per year.
- The **p-value was $$<<0.0001$$**, meaning the difference is statistically significant.
- Since the difference in means is much larger than what we'd expect by random chance, we **reject the null hypothesis**.
- This suggests that **men received significantly higher salary increases than women** over the years.

## **Promotion Time: No Clear Evidence of Bias**

Next, we analyzed whether there were differences in **time taken for promotion**. A similar hypothesis test was conducted to compare promotion durations between men and women.

- The **median promotion time for both male and female faculty was 7 years**.
- The **p-value of $0.1390$** indicates **no statistically significant difference**.
- Since we don’t have strong evidence that men and women take different amounts of time to get promoted, we **fail to reject the null hypothesis**.
- This suggests that, based on this data, **promotion timelines appear to be similar across genders**.

## **Conclusion**

Our findings paint a mixed picture:
- **No strong evidence of bias in promotion time** – both men and women took around $7 years$ to get promoted.
- **Clear evidence of bias in salary increases** – men received significantly higher yearly raises than women.

Even if men and women are promoted at similar rates, the **disparity in salary growth over time can contribute to long-term pay gaps**. This raises important questions about salary transparency and fairness in academic institutions.

Identifying such biases is the first step toward addressing them. We hope these insights contribute to discussions on **ensuring fairer salary policies and greater transparency in university pay structures**.
