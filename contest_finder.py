import streamlit as st

file_path = "canada_contests.txt"  # Make sure this is exact

contests = []
try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                name, description, url = parts
                contests.append({"name": name, "description": description, "url": url})
except FileNotFoundError:
    st.error(f"File not found: {file_path}")

st.title("🎯 Canadian Contest Finder")
st.write(f"Found {len(contests)} Canadian contests:")

for c in contests:
    st.markdown(f"• [{c['name']}]({c['url']})  \n{c['description']}")