# 1. Uncovering the Story in the Data: An Overview and EDA

Welcome to the first installment of our blog series on investigating faculty salary data at a US university. In this post, we’re taking a close look at the raw data and sharing our initial findings through a detailed exploratory data analysis (EDA). Our goal is to tell the story behind the numbers—what do the features tell us about the faculty and their careers? And what interesting trends or outliers can we uncover?

---

## Getting to Know the Data

Our dataset is a rich collection of records representing yearly snapshots of 1,597 faculty members. Each record includes information such as:
- **Personal and Academic Details:** An identification number, sex, and details about the highest degree earned (e.g., PhD, professional, or other).
- **Timing Milestones:** The year the faculty member attained their highest degree (*yrdeg*), the year they were hired (*startyr*), and the current year in the record (*year*).
- **Job-Related Variables:** Their academic rank (Assistant, Associate, or Full Professor) and an indicator for whether they held administrative roles.
- **Compensation:** The monthly salary for that specific year.

What makes the dataset even more interesting is that some features (like sex, degree type, and year of highest degree) remain constant over time, while others (like salary, rank, and administrative status) evolve year after year. This structure provides a dynamic view of how a faculty career progresses.

## A Closer Look at the Features

Before diving into the numbers, it’s useful to understand what each variable represents:

- **Case and ID:** Every record is tagged with a unique case number and an identification number that links records belonging to the same faculty member.
- **Sex:** This tells us whether the faculty member is male or female. Later in our analysis, we’ll explore how this variable relates to salary differences.
- **Degree (deg) and Year of Degree (yrdeg):** These provide insight into the educational background of our faculty. For instance, our descriptive analysis shows that on average, women completed their degrees later (around 1981) compared to men (around 1974).
- **Field:** Faculty are grouped into categories such as Arts, Professional (fields like Business, Law, or Engineering), and Other. This helps us see if salary trends differ by academic discipline.
- **Start Year (startyr) and Year:** These variables allow us to track career progression. It turns out that on average, women were hired around 1985, while men joined the university around 1979—a detail that hints at differences in experience.
- **Rank and Admin:** The rank indicates the career stage (Assistant, Associate, Full) and the admin variable flags if the faculty member had additional responsibilities (like serving as a department chair).
- **Salary:** Recorded as the monthly salary in dollars, this is our primary quantitative measure and one of the key indicators in our analysis.

## What Do the Numbers Tell Us? – Descriptive Insights

Our initial descriptive analysis revealed several interesting points:
- **Faculty Distribution:** Out of 1,597 faculty members, approximately 25% (409) are women and 75% (1,188) are men. This imbalance sets the stage for exploring potential disparities.
- **Educational and Hiring Trends:** Looking at the boxplot, women earned their highest degrees later than men. Similarly, women were hired at the university a few years after their male colleagues. This suggests a potential generational or systemic difference in career trajectories.
- **Salary Differences:** One of the most striking findings is the salary gap. The median monthly salary in 1995 was about \$5,400 for women compared to \$6,700 for men. Not only does the gap exist in the medians, but the range also shows that the highest salaries tend to be concentrated among men.
- **Rank and Representation:** When we examine academic ranks, we see that women hold less than half of the positions in each rank category. For example, among faculty with a PhD—a group of 1,350—the number of women is roughly one-quarter (about 334), highlighting a gender imbalance in the most senior ranks.

## Outliers and Interesting Trends

While the numbers give us overall trends, our EDA has also helped us spot a few outliers and curious patterns:
- **Salary Extremes:** There are a few instances where salaries are exceptionally high compared to the norm. These outliers might be linked to specific administrative roles or other factors not captured by the basic variables.
- **Time Trends in Salary Growth:** Because our data spans nearly two decades, you can observe how salaries have generally trended upward over time. However, the rate of increase isn’t uniform. In some instances, the salary growth appears more gradual, while in others there are steeper jumps. Such variations can spark questions about promotions or changes in university policies over time.
- **Career Progression:** Beyond the salary, the data also hints at interesting differences in career trajectories. For example, the delay in attaining higher degrees or being hired could influence the pace of promotions. These trends set the stage for our later, more formal statistical analyses.

## Visualizing the Distributions

Understanding a dataset isn’t just about numbers—it’s also about seeing patterns visually. In our upcoming posts (and even within our interactive web app), we plan to present:
- **Histograms and Boxplots:** These will help illustrate the distribution of salaries by sex, rank, and field. For instance, boxplots can quickly show the median, spread, and any outliers in salary distributions.
- **Trend Lines Over Time:** Line graphs will show how salaries have increased over the years, helping us understand whether the gap between men and women has widened or narrowed.
- **Bar Charts for Categorical Data:** Visualizations of academic rank and field distributions will provide a clearer picture of how faculty demographics are structured.

## Wrapping Up the EDA

This first blog post serves as an introduction to our dataset and the initial EDA phase. By breaking down the features, identifying key trends, and spotting outliers, we’ve set a strong foundation for our deeper statistical analysis in future posts. Our next steps will involve rigorously testing hypotheses—like whether salary differences between men and women are statistically significant—and assessing the impact of potential confounding factors.


Stay tuned for our next installments where we dive into the statistical methods and inference behind these findings, and begin to address the core questions of sex bias and promotion patterns.

We hope this overview gives you a clear, accessible entry point into this dataset. It’s exciting to see how raw data can reveal compelling narratives about career trajectories, equity, and institutional practices. Join us next time as we unravel more of these insights with formal statistical tests and in-depth analysis!
