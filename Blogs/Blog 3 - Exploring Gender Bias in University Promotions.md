# 3. Exploring Gender Bias in University Promotions

Wewlcome to the third installment of the blog series we will be analyzing gender bias in university promotions using historical data (1980-1995). While promotion timelines appear similar for men and women, salary increases show a significant disparity. Data-driven insights highlight the need for fairer salary policies in academia.

---

## **Introduction**

Discussions around gender bias in workplace promotions are nothing new, and universities are no exception. To explore whether men and women experience differences in promotion time and salary increases in academia, we analyzed **promotion data from 1980 to 1995**.

To make the study fair and avoid skewed results, we **excluded faculty members who had been in their current roles for less than 7 years**, as that was the **median promotion time** across genders. This helped ensure that no one was unfairly included just because they had recently been promoted.

We focused on two key questions:
1. **Are salary increases different for male and female faculty?**
2. **Do men and women take different amounts of time to get promoted?**

## **Salary Increases: Evidence of Bias**

To check if men and women received different salary increments per year, we conducted a **t-test** comparing their yearly salary increases.

### **Methodology**

- We computed **each faculty member’s total salary increase** over the period by taking the difference between their **final and initial salary**.
- This was then **divided by the number of years** to obtain an **average yearly increase (salary increase slope)**.
- A **two-sample t-test** was performed to compare the average salary increase slopes between male and female faculty.

### **Confounders**

- Factors such as **rank, performance, or administrative responsibilities** could influence salary increases, but these were **not adjusted for** in this analysis. The focus remains on the **relationship between sex and salary increase**.

### **Conclusion**

- Male faculty received an average salary increase of \$260 per year, while female faculty received \$210 per year.
- The **p-value was $$<<0.0001$$**, meaning the difference is statistically significant.
- Since the difference in means is much larger than what we'd expect by random chance, we **reject the null hypothesis**.
- This suggests that **men received significantly higher salary increases than women** over the years.
- While this points to potential **gender bias in salary increments**, it’s important to consider that sample size disparities may impact the reliability of these estimates.


## **Promotion Time: No Clear Evidence of Bias**

Next, we analyzed whether there were differences in **time taken for promotion**. A similar hypothesis test was conducted to compare promotion durations between men and women.

### **Promotion Time Analysis (Two-Sample T-Test)**

We calculated the number of years it took for faculty members to be promoted from **Associate to Full Professor** using the formula:

$promotion time = rank end year - rank start year + 1$

A **two-sample t-test** was then performed to compare the **average promotion time** between male and female faculty.

- The **median promotion time for both male and female faculty was 7 years**.
- The **p-value of $0.1390$** indicates **no statistically significant difference**.
- Since we don’t have strong evidence that men and women take different amounts of time to get promoted, we **fail to reject the null hypothesis**.
- This suggests that, based on this data, **promotion timelines appear to be similar across genders**.

## **Promotion Proportion Analysis: No Clear Evidence of Bias**

Since promotion timing alone does not capture the full picture, we also analyzed the **proportion of faculty promoted**.

### **Methodology**

- We compared the proportion of faculty promoted (from Associate to Full Professor) **between genders**.
- A **two-proportion z-test** was used to determine whether promotion rates significantly differed by gender.
- To ensure fairness, we focused on faculty members who had been at their rank **long enough to be considered eligible for promotion**.

### **Consideration of Sample Size**

- The sample sizes for promoted and non-promoted groups were unbalanced:
  - **Promoted Group**: **447 males, 100 females**
  - **Non-Promoted Eligible Group**: **746 males, 238 females**
- However, the z-test accounts for these differences in group sizes.

### **Interpretation**

- With a **p-value of 0.444 (> 0.05)**, we **fail to reject the null hypothesis**.
- This indicates **no significant difference in the proportion of promotions** between male and female faculty.

---

## **Overall Conclusion**

Our findings provide a nuanced perspective on gender bias in university promotions:

1. **Salary Increases Show Gender Disparity**  
   - Male faculty received **significantly higher salary increases per year** than female faculty (**\$260 vs. \$210 per year**).  
   - The difference was **statistically significant**, suggesting potential **bias in salary increments**.  

2. **No Strong Evidence of Bias in Promotion Time or Rates**  
   - Faculty members of both genders took a **median of 7 years** to get promoted.  
   - The **promotion rate** was **not significantly different** between men and women.  
   - Both the **t-test and z-test failed to reject the null hypothesis**, indicating that **promotion timelines and rates appear fair**.

While **promotion timelines seem equitable**, the **disparity in salary increases raises important concerns**. Over time, this can **contribute to long-term pay gaps**, affecting financial stability and career progression.  

This analysis highlights the need for **greater transparency in salary policies within academia**, ensuring that faculty members are compensated fairly, regardless of gender.
