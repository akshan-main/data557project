import pandas as pd

def load_data():
    df = pd.read_csv("salary.txt", delim_whitespace=True)
    df["pre_emp_gap"] = df["startyr"] - df["yrdeg"]  
    df["promotion_time"] = df.groupby("id")["rank"].transform(lambda x: (x == "Assoc").cumsum())
    return df