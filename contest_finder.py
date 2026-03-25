import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Canadian Contest Finder", layout="wide")
st.title("🎯 Canadian Contest Finder")

# Example site to scrape
URL = "https://www.canadianfreestuff.com/canadian-contests/"  # You can add more sources

def fetch_contests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    contests = []

    # Each site is different — example uses h3 titles and description below
    for item in soup.find_all("div", class_="contest-item"):  # adjust based on site HTML
        name_tag = item.find("h3")
        desc_tag = item.find("p")
        link_tag = item.find("a", href=True)

        if name_tag and link_tag:
            contest = {
                "name": name_tag.get_text(strip=True),
                "description": desc_tag.get_text(strip=True) if desc_tag else "",
                "url": link_tag["href"]
            }
            contests.append(contest)

    return contests

all_contests = fetch_contests(URL)

# Deduplicate by name
unique_contests = []
seen = set()
for c in all_contests:
    if c["name"] not in seen:
        unique_contests.append(c)
        seen.add(c["name"])

st.write(f"Found {len(unique_contests)} Canadian contests:")

for contest in unique_contests:
    st.markdown(f"- [{contest['name']}]({contest['url']})  \n{contest['description']}")