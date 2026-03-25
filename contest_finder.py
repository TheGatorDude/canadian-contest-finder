# contest_finder.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------

# Replace these with real Canadian contest URLs
CONTEST_SITES = [
    "https://www.redflagdeals.com/forums/forumdisplay.php?f=51",  # giveaways forum
    "https://www.canadiangiveawayblog.com"  # example blog
]

OUTPUT_FILE = "canada_contests_all_sites.txt"

# -----------------------------
# Functions
# -----------------------------

def fetch_contests(url):
    """Fetch contest titles from a site. Returns list of strings or None on failure."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        st.warning(f"Failed to fetch {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, "lxml")
    contests = []

    # Try to grab <a> tags with relevant keywords
    for link in soup.find_all("a"):
        text = link.get_text(strip=True)
        if text and ("contest" in text.lower() or "giveaway" in text.lower()):
            contests.append(text)

    return contests

def save_contests(contest_list):
    """Append contests to OUTPUT_FILE with timestamp."""
    if not contest_list:
        return

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        for contest in contest_list:
            f.write(f"{datetime.now().isoformat()} - {contest}\n")

# -----------------------------
# Streamlit App
# -----------------------------

st.title("Canadian Contest Finder")
st.write("Collects contests from multiple Canadian websites.")

if st.button("Fetch Contests"):
    total_found = 0
    for site in CONTEST_SITES:
        st.info(f"Fetching from {site}...")
        contests = fetch_contests(site)
        if contests:
            total_found += len(contests)
            st.success(f"Found {len(contests)} contests on {site}")
            save_contests(contests)
            for c in contests:
                st.write(f"- {c}")
        else:
            st.error(f"No contests found or failed to fetch {site}")

    st.write(f"Total contests found this run: {total_found}")