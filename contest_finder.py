import streamlit as st

st.set_page_config(page_title="Canadian Contest Finder", layout="wide")

# Example: loading contests from a text file
# Format in file: name|description|url
# You can replace 'canada_contests_all_sites.txt' with your own source
def load_contests(file_path="canada_contests_all_sites.txt"):
    contests = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "|" not in line:
                    continue
                name, description, url = line.split("|")
                contests.append({"name": name.strip(), "description": description.strip(), "url": url.strip()})
    except FileNotFoundError:
        st.error(f"Contest source file not found: {file_path}")
    return contests

# Remove duplicates by contest name
def deduplicate_contests(contests):
    seen = set()
    deduped = []
    for c in contests:
        if c["name"] not in seen:
            deduped.append(c)
            seen.add(c["name"])
    return deduped

contests = load_contests()
contests = deduplicate_contests(contests)

st.title("🎯 Canadian Contest Finder")
st.write(f"Found {len(contests)} Canadian contests:")

for contest in contests:
    st.markdown(f"• [{contest['name']}]({contest['url']})  \n{contest['description']}")