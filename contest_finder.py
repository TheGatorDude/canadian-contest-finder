import streamlit as st

st.set_page_config(page_title="Canadian Contest Finder", layout="wide")

file_path = "canada_contests.txt"

def load_contests(file_path):
    contests = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name, description, url = parts
                    # Simple priority scoring example
                    priority = 1
                    keywords = ["Trip", "Vacation", "Gift Card", "Cash", "iPhone", "Apple Watch"]
                    for kw in keywords:
                        if kw.lower() in description.lower():
                            priority += 1
                    contests.append({
                        "name": name,
                        "description": description,
                        "url": url,
                        "priority": priority
                    })
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    return contests

contests = load_contests(file_path)

st.title("🎯 Canadian Contest Finder")
st.write(f"Found {len(contests)} Canadian contests:")

# Optional: sort by priority
contests = sorted(contests, key=lambda x: x["priority"], reverse=True)

for c in contests:
    st.markdown(f"• [{c['name']}]({c['url']})  \n{c['description']}\nPriority: {c['priority']}")