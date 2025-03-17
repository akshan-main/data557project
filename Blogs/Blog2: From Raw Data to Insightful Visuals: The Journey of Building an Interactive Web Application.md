# From Raw Data to Insightful Visuals: The Journey of Building an Interactive Web Application

Welcome to the second installment of our blog series on investigating faculty salary data at a US university. In this post, we would like to shed light on how to transform the rough data into meaningful insights. 

It all started with a dataset — a plain text file filled with numbers and categorical variables. Faculty salaries, degrees, ranks, and years of service were all there, waiting to tell a story. But the challenge was clear: how could we transform this static dataset into an interactive, engaging and intuitive experience?  

We knew that rows and columns of numbers alone wouldn’t cut it. We needed **visualization** - but not just any charts. They had to be meaningful, dynamic and easy to explore. The journey began with choosing the right tech stack, designing a smooth user experience and selecting the best charts to bring the data to life.  

---

## **Why Streamlit?**  

When faced with a project like this, the first question is always: *What tools should we use?*  

We wanted something **fast, interactive, and Python-friendly**, so **Streamlit** was the natural choice. It allowed us to build a sleek web app without the need for complex frontend coding. With just a few lines of code, we could create widgets, filter data in real-time, and display visualizations dynamically.  

For **data manipulation**, we relied on **Pandas**, the Swiss army knife for handling datasets. And for visualization? **Matplotlib and Seaborn** were our go-to libraries. They provided **beautiful, customizable** plots while seamlessly integrating with Pandas.  

With our tools in place, it was time to think about **how users would interact with the data**.  

---

## **Designing a User Experience That Feels Effortless**  

Have you ever landed on a dashboard so cluttered that you didn’t know where to start? We didn’t want that.  

Initially, we placed **filters at the top of the page**, but it quickly became clear: they were taking up too much space. So, we **moved them to a sidebar**, keeping the main page clean and focused on **the data itself**.  

We also needed to answer a key question: *What should users see first?*  

- A **fixed "Data Overview" section** provided a **quick summary** of faculty demographics.  
- **Dynamic visualizations** adapted based on what users wanted to explore.  
- **Textual insights** accompanied each visualization, ensuring users could interpret the charts correctly.  

With the user flow in place, it was time for the most exciting part: **bringing the data to life with charts**.  

---

## **The Art of Choosing the Right Charts**  

Visualizing data isn’t just about throwing charts onto a page. Each graph must serve a **specific purpose**. Here’s how we approached it:  

### **1. Exploring Salary Disparities**  

We started with **boxplots**—the perfect tool for highlighting salary distributions. Were there **outliers**? Were **female faculty members** earning less on average? The boxplots revealed these patterns instantly.  

But numbers tell half the story, so we added **summary statistics**—mean, median, min, and max values—to provide a numerical backbone. To wrap it up, a **histogram with KDE (Kernel Density Estimation)** helped compare salary distributions between men and women.  

### **2. Academic Ranks: Who Holds the Highest Positions?**  

To visualize the distribution of **Assistant, Associate, and Full Professors**, we used **stacked bar charts**. Instead of raw counts, we calculated **percentages**, making it easier to compare across groups.  

A **summary table** complemented the chart, offering a **precise breakdown** of faculty ranks by gender.  

### **3. Career Progression Over Time**  

To explore **hiring trends**, we turned to **boxplots** again—this time, for **Start Year and Degree Year**. Were men being hired at younger ages? Were women obtaining PhDs later in their careers? These plots helped us uncover such trends.  

For further insights, we included **summary statistics**, providing a **numerical snapshot** of career trajectories.  

### **4. Academic Fields: Who Works Where?**  

Did gender influence which academic fields faculty members specialized in? **Stacked bar charts** made it easy to compare distributions across **Arts, Professional Schools, and Other Fields**.  

Again, **percentages over raw counts** made the data more digestible, and a **summary table** provided an exact breakdown.  

---

## **Challenges We Faced Along the Way**  

Of course, no project is without its challenges. Here are a few things we had to overcome:  

1. **Handling Duplicate Records**  
   - Since faculty members appeared multiple times across years, we had to ensure we weren’t **double-counting individuals**. By filtering **unique IDs**, we kept the data clean.  

2. **Balancing Interactivity with Performance**  
   - Real-time filtering was **powerful but resource-intensive**. We optimized by pre-computing summaries and **only rendering charts when needed**.  

3. **Ensuring Clarity in Data Representation**  
   - Some initial charts felt **misleading** (e.g., raw counts instead of percentages). Switching to **relative distributions** made comparisons much easier.  

---

## **Final Thoughts: The Power of Interactive Data Visualization**  

This project reinforced an important lesson: **data alone isn’t enough**. The way we **present and interact** with it determines whether we uncover **valuable insights or miss the bigger picture**.  

By choosing the **right tech stack**, focusing on **user experience**, and selecting **the best visualizations**, we transformed a raw dataset into an **engaging and interactive** experience.  

Looking ahead, we could further enhance the dashboard by:  
- Adding **tooltips** for deeper insights.  
- Allowing users to **download filtered data**.  
- Exploring **trend analysis over multiple years**.  

But for now, we step back and admire the journey—from **plain text to interactive storytelling**.  
