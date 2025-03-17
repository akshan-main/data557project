import streamlit as st
import os

BLOG_DIR = "./Blogs/"

def extract_description(lines):
    description_lines = []
    for line in lines[1:]:  # Skip the title line
        if line.strip() == "---":
            break
        description_lines.append(line.strip())
    return " ".join(description_lines)

def load_blog_metadata():
    """Reads markdown blog files and extracts title + short description."""
    blogs = []
    for filename in os.listdir(BLOG_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(BLOG_DIR, filename), "r", encoding="utf-8") as file:
                lines = file.readlines()
                title = lines[0].strip("# ").strip()
                description = extract_description(lines)
                blogs.append({"title": title, "description": description, "file": filename})
    return sorted(blogs, key=lambda b: b["title"])

def reset_selection():
    """Callback to reset the blog selection and drop-down choice."""
    st.session_state["selected_blog"] = None
    st.session_state["selected_title"] = "(None)"

def display_blog_content():
    """Displays the full blog content if a blog is selected."""
    blog_file = st.session_state.get("selected_blog")
    if blog_file:
        with open(os.path.join(BLOG_DIR, blog_file), "r", encoding="utf-8") as file:
            content = file.read()
        st.markdown(content)

        # Use the on_click callback so we don't attempt to directly set session_state keys here
        st.button("Back to Blogs", on_click=reset_selection)

def display_blog_list():
    """Displays all blogs in 2 columns with short descriptions and read-more buttons."""
    blogs = load_blog_metadata()
    cols = st.columns(2)

    for i, blog in enumerate(blogs):
        with cols[i % 2]:
            st.subheader(blog["title"])
            st.write(blog["description"])
            if st.button("Read More", key=blog["file"]):
                st.session_state["selected_blog"] = blog["file"]
                st.rerun()

# ------------------ MAIN SCRIPT ------------------
st.sidebar.title("Blog Navigator")

# 1) Load metadata
all_blogs = load_blog_metadata()

# 2) Build the list for the selectbox
blog_titles = [b["title"] for b in all_blogs]
title_to_file = {b["title"]: b["file"] for b in all_blogs}

# Ensure we have session keys
if "selected_title" not in st.session_state:
    st.session_state["selected_title"] = "(None)"

# 3) Create the selectbox in sidebar
chosen = st.sidebar.selectbox(
    "Select a Blog:",
    ["(None)"] + blog_titles,
    key="selected_title"
)

# If the user picks from the selectbox, set the blog in session_state
if st.session_state["selected_title"] != "(None)":
    title = st.session_state["selected_title"]
    st.session_state["selected_blog"] = title_to_file[title]

# Display either the chosen blog or the list
if st.session_state.get("selected_blog"):
    display_blog_content()
else:
    display_blog_list()
