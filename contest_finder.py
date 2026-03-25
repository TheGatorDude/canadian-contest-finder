import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎯 Canadian Contest Finder", layout="wide")

st.title("🎯 Canadian Contest Finder")
st.markdown("Find Canadian contests across multiple sources with priority scoring!")

# Keywords for high-priority contests
priority_keywords = ["cash", "gift card", "trip", "vacation", "electronics", "laptop", "phone", "watch", "voucher", "prize", "tablet", "TV", "air miles"]

# User input filter
filter_keyword = st.text_input("Filter contests by keyword (optional):").lower().strip()

# Sources to scrape
sources = {
    "Canadian Free Stuff": "https://www.canadianfreestuff.com/canadian-contests/",
    "Contest Scoop": "https://www.contestscoop.com/canadian-contests/"
}

# Function to fetch contests from a URL
def fetch_contests(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text
    except Exception as e:
        st.warning(f"Failed to fetch from {url}: {e}")
        return ""

# Function to parse contests (simple text scraping)
def parse_contests(text, source_name):
    # This is a basic parsing: find all hyperlinks and their text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    contests = []
    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        href = link["href"]
        if title and "canada" in title.lower():
            contests.append({
                "Source": source_name,
                "Title": title,
                "Link": href
            })
    return contests

# Collect all contests
all_contests = []
for name, url in sources.items():
    html = fetch_contests(url)
    all_contests.extend(parse_contests(html, name))

# Apply filter if user entered one
if filter_keyword:
    all_contests = [c for c in all_contests if filter_keyword in c["Title"].lower()]

# Compute priority score
def score_contest(title):
    score = sum(1 for kw in priority_keywords if kw in title.lower())
    return score

for c in all_contests:
    c["Priority"] = score_contest(c["Title"])

# Sort by priority
all_contests.sort(key=lambda x: x["Priority"], reverse=True)

# Display contests in a nice table
if all_contests:
    df = pd.DataFrame(all_contests)
    df["Link"] = df.apply(lambda row: f"[Link]({row['Link']})", axis=1)
    df = df[["Source", "Title", "Link", "Priority"]]
    st.markdown(f"### Found {len(df)} Canadian contests:")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No contests found. Try changing the filter or check back later!")

# Optional: save to a file
if st.button("Save contests to CSV"):
    pd.DataFrame(all_contests).to_csv("canadian_contests.csv", index=False)
    st.success("Saved contests to canadian_contests.csv")