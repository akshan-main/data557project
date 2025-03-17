import streamlit as st
import os

BLOG_DIR = "./Blogs/"

def extract_description(lines):
    description_lines = []
    for line in lines[1:]:  # Skip the title line
        if line.strip() == "---":
            break
        description_lines.append(line.strip())
    return " ".join(description_lines)  # Join multiple lines into a single string

def load_blog_metadata():
    """Reads all markdown blog files and extracts title + description."""
    blogs = []
    for filename in os.listdir(BLOG_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(BLOG_DIR, filename), "r", encoding="utf-8") as file:
                lines = file.readlines()
                title = lines[0].strip("# ").strip()  # Extract title from first line
                description = extract_description(lines)  # Extract short description
                blogs.append({"title": title, "description": description, "file": filename})
    sorted_blogs = sorted(blogs, key=lambda k: k["title"])
    return sorted_blogs

def display_blog_content():
    """Displays the full blog content when selected."""
    blog_file = st.session_state.get("selected_blog")
    if blog_file:
        with open(os.path.join(BLOG_DIR, blog_file), "r", encoding="utf-8") as file:
            content = file.read()
        st.markdown(content)
        if st.button("Back to Blogs"):
            del st.session_state["selected_blog"]
            st.rerun()

def display_blog_list():
    """Displays blogs in a 2-column layout on the main page."""
    blogs = load_blog_metadata()
    cols = st.columns(2)

    for i, blog in enumerate(blogs):
        with cols[i % 2]:
            st.subheader(blog["title"])
            st.write(blog["description"])
            # "Read More" button also sets the selected_blog
            if st.button("Read More", key=blog["file"]):
                st.session_state["selected_blog"] = blog["file"]
                st.rerun()

# ------------------------
# Main Script
# ------------------------
st.sidebar.title("Blog")

# 1) Load metadata once
all_blogs = load_blog_metadata()

# 2) Build a list of titles for the sidebar
blog_titles = [b["title"] for b in all_blogs]
title_to_file = {b["title"]: b["file"] for b in all_blogs}

# 3) Create a sidebar selectbox (or radio buttons) with blog titles
selected_title = st.sidebar.selectbox("Select a Blog:", ["(None)"] + blog_titles)

# 4) If the user picks a blog from the selectbox, set the session state
if selected_title != "(None)":
    st.session_state["selected_blog"] = title_to_file[selected_title]

# 5) Display either the chosen blog or the list of blogs
if "selected_blog" in st.session_state:
    display_blog_content()
else:
    display_blog_list()
