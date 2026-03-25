import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("🎯 Canadian Contest Finder")

# Example contest source
URLS = [
    "https://www.contestsite1.ca",
    "https://www.contestsite2.ca",
]

all_contests = []

for url in URLS:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        for contest in soup.select(".contest-entry"):  # adjust selector to site
            title = contest.select_one(".title").get_text(strip=True)
            description = contest.select_one(".description").get_text(strip=True)
            link = contest.select_one("a")["href"]
            all_contests.append({
                "title": title,
                "description": description,
                "link": link
            })
    except Exception as e:
        st.warning(f"Failed to fetch {url}: {e}")

# Remove duplicates
df = pd.DataFrame(all_contests).drop_duplicates(subset=["title"])

st.write(f"Found {len(df)} Canadian contests:")

for idx, row in df.iterrows():
    st.markdown(f"• [{row['title']}]({row['link']})  \n{row['description']}")