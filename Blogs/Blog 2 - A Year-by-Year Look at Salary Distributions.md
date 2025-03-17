# 2. A Year-by-Year Look at Salary Distributions

Welcome to the second  installment of our blog series on investigating faculty salary data at a US university. This blog explores a 19‐year dataset of salary distributions from 1976 to 1995, focusing on whether the average salaries of two groups (often men vs. women) differ significantly each year.

---

## Understanding the Data: 1976 to 1995

1. **Yearly Salary Distribution Plots**  
   - Each of the 19 images shows a distribution for two groups in that specific year i.e men and women.  
   - Accompanying each distribution, a **summary** table or annotation typically lists:
     - Mean salary for each group,  
     - Estimated difference in means,  
     - Standard error,  
     - t‐value and p‐value.

2. **Consistent Pattern**  
   - Across all 19 years, the **difference in mean salaries** is not only nonzero but also **large enough** that the t‐test yields a p‐value **well below** any conventional significance threshold (e.g., p < 0.05).  
   - The null hypothesis states “the two groups have equal means,” but the data robustly reject that notion year after year.

---

## Key Observations Year by Year

### 1976
- **Difference in Means**: The earliest year reveals a salary gap of a few hundred dollars.  
- **T‐value**: Roughly 5–6 in the visual summary (well above the typical cutoff ~2 for significance).  
- **P‐value**: Very small (often < 0.001).  
- This sets the stage: from the mid‐1970s, a gap is visible.

### 1977–1980
- Each subsequent year extends that gap, sometimes **increasing** by another \$100–\$200.  
- The t‐values hover in the **4–8 range**, reaffirming that each year’s difference is unlikely to be random fluctuation.  
- By 1980, the difference is considerably larger than in 1976, suggesting the gap might be **widening** in the late 1970s.

### 1981–1985
- For some years, the gap stabilizes (e.g., 1982 and 1983 show similar means).  
- In 1985, the difference grows again by a few hundred dollars, leading to one of the largest t‐values in the entire dataset.

### 1986–1990
- The **mid‐to‐late 1980s** images frequently show a difference of around \$1,000 or more, with t‐values up in the 6–10 range.  
- This implies the two groups are diverging further or, at least, not converging in mean salary.

### 1991–1995
- By the early 1990s, the difference seems consistently over \$1,000.  
- T‐values remain high (5–12), and p‐values are effectively zero to many decimal places.  
- The final 1995 image (year 19) closes the series with a continuing large gap—again, no sign that the two means have converged.

---

## Interpreting the Consistently Significant Gap

1. **Null Hypothesis Always Rejected**  
   - Every year, the test statistic (t‐value) far exceeds the typical cutoff for significance, so we never accept the notion of “no salary difference.”  
   - The uniformity of these results underscores a **persistent structural difference** in pay.

2. **Possible Explanations**  
   - **Hiring Practices**: If one group consistently starts at higher salaries, the yearly gap might remain or expand.  
   - **Annual Raises**: Even if starting pay were equal, differences in raises could cause a persistent gap.  
   - **Market or Policy Changes**: If the difference does not shrink, new policy attempts (if any occurred) apparently had limited effect, or external labor market factors perpetuated the gap.

3. **Visual Confirmations**  
   - The shapes of the distributions in each image often show the group in question has a **right‐shifted** (higher‐pay) distribution.  
   - The means rarely (if ever) overlap, consistent with a large t‐value each time.

---

## Why a Year‐by‐Year Lens Matters

Had we examined **just one or two** random years, we might question whether the gap was a temporary phenomenon. But the 19 consecutive images (1976–1995) show that:

- The gap **did not vanish** or **reverse** in any single year.  
- The **magnitude** might fluctuate slightly year to year (some years ~\$800 difference, others ~\$1,300), but never close to zero.  
- This strongly suggests that attempts (if any) to address pay disparity did **not** yield major changes in this 20-year window.

---
## Starting Salary: Evidence Across All Years

- **Aggregated View**: In addition to the year-by-year breakdown, we have a **combined distribution** showing starting salaries across the entire timespan.  
- **Mean Male Starting Salary**: \$4,855  
- **Mean Female Starting Salary**: \$4,185  
- **Difference**: ~\$670  
- **T‐value**: 4.13 (p < 0.001)

**Key Insight**  
This aggregated starting-salary distribution confirms the pattern we see annually: a **significant** difference, even at the first salary an employee receives. In other words, men do not simply pull ahead through raises over time; they’re also beginning at a higher level from the get-go. Seeing this effect hold in the combined data (as well as year by year) underscores just how embedded the gap is.

---

## Conclusions

1. **Persistence**: A consistent salary gap from 1976 to 1995, each year with a statistically significant difference, indicates **long-standing pay inequality**.  
2. **Magnitude Variation**: While the gap’s size changes somewhat (some years bigger, some smaller), it **always** surpasses the standard error enough to produce a large t‐value.  
3. **Policy Implications**: If the organization or industry behind this data aims to ensure fairness, it must do more than short‐term fixes. The fact that the gap remains for nearly two decades underscores the need for **systemic** changes—be it in hiring offers, wage increments, or thorough salary audits.

**Key Takeaway**: The **t‐test** consistently rejects the null across every year’s salary data from 1976 to 1995. No single year offers evidence that these two groups have the same pay distribution, pointing to a deeply **embedded** pay gap. 

In our next blog, we will delve into **Exploring Gender Bias in University Promotions**. We will analyze promotion rates, time to promotion, and other relevant metrics to uncover any disparities and discuss potential underlying causes and solutions.

Stay tuned for more insights!