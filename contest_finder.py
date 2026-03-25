# contest_finder.py
import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Canadian Contest Finder", layout="wide")
st.title("🎯 Canadian Contest Finder")

# --- SOURCES ---
sources = {
    "Canadian Free Stuff": "https://www.canadianfreestuff.com/canadian-contests/",
    "Contest Scoop": "https://www.contestscoop.com/canadian-contests/",
    "Reddit Sweepstakes": "https://www.reddit.com/r/sweepstakes/.json",
    "Gleam": "https://gleam.io",
    "Kingsumo": "https://kingsumo.com",
}

# Keywords for scoring big prizes
priority_keywords = ["$1000", "$500", "$2500", "vacation", "trip", "airplane", "electronics", "PS5", "Xbox", "MacBook", "iPhone"]

# Function to fetch and parse contests from a URL
def fetch_contests(url, source_name):
    contests = []
    try:
        if "reddit" in url:
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            data = r.json()
            for post in data["data"]["children"]:
                title = post["data"]["title"]
                link = post["data"]["url"]
                if "canada" in title.lower():
                    contests.append((source_name, title, link))
        else:
            r = requests.get(url)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.find_all("a", href=True):
                text = a.get_text(strip=True)
                href = a["href"]
                if "canada" in text.lower() and href.startswith("http"):
                    contests.append((source_name, text, href))
    except Exception as e:
        st.warning(f"Failed to fetch {source_name}: {e}")
    return contests

# Function to score contests by priority
def score_contest(title):
    score = sum(1 for kw in priority_keywords if kw.lower() in title.lower())
    return score

# --- MAIN SCRAPER ---
all_contests = []

for name, url in sources.items():
    contests = fetch_contests(url, name)
    all_contests.extend(contests)

if all_contests:
    # Build dataframe
    df = pd.DataFrame(all_contests, columns=["Source", "Title", "Link"])
    df["Score"] = df["Title"].apply(score_contest)
    df = df.sort_values(by="Score", ascending=False)

    st.markdown(f"### Found {len(df)} Canadian contests:")

    # Display as clickable links
    def make_clickable(url, text):
        return f'<a href="{url}" target="_blank">{text}</a>'

    df_display = df.copy()
    df_display["Title"] = df_display.apply(lambda x: make_clickable(x["Link"], x["Title"]), axis=1)
    st.write(
        df_display[["Source", "Title", "Score"]].to_html(escape=False, index=False),
        unsafe_allow_html=True
    )
else:
    st.info("No Canada contests found!")