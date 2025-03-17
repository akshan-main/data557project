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
    return blogs.sort()

def display_blog_list():
    """Displays blogs in a 3-column grid layout."""
    blogs = load_blog_metadata()
    cols = st.columns(2)  # Create 2 columns

    for i, blog in enumerate(blogs):
        with cols[i % 2]:  # Distribute across 2 columns
            st.subheader(blog["title"])
            st.write(blog["description"])
            if st.button(f"Read More", key=blog["file"]):
                st.session_state["selected_blog"] = blog["file"]
                st.rerun()

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

# Sidebar navigation
st.sidebar.title("Blog")

if "selected_blog" in st.session_state:
    display_blog_content()
else:
    display_blog_list()
