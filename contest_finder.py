# contest_finder.py

import streamlit as st
import requests
from bs4 import BeautifulSoup

# List of contest sites (replace placeholders with real sites)
CONTEST_SITES = [
    "https://www.contestsite1.ca",
    "https://www.contestsite2.ca",
    "https://www.contestsite3.ca"
]

def fetch_contests(url):
    """Fetch contests from a site, return list of (title, description, link)."""
    contests = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Example: find all links in <a> tags inside a contest listing
        for a in soup.find_all("a", href=True):
            title = a.get_text(strip=True)
            link = a["href"]
            # Optional: grab description from sibling or data attributes
            desc_tag = a.find_next_sibling("p")
            description = desc_tag.get_text(strip=True) if desc_tag else ""
            if title:
                contests.append((title, description, link))
                
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
    return contests

def main():
    st.title("🎯 Canadian Contest Finder")
    
    all_contests = []
    for site in CONTEST_SITES:
        site_contests = fetch_contests(site)
        all_contests.extend(site_contests)

    # Remove duplicates based on title
    unique = {}
    for title, desc, link in all_contests:
        if title not in unique:
            unique[title] = (desc, link)

    if unique:
        st.write(f"Found {len(unique)} Canadian contests:")
        for title, (desc, link) in unique.items():
            st.markdown(f"• [{title}]({link})")
            if desc:
                st.markdown(f"  {desc}")
    else:
        st.write("Found 0 Canadian contests.")

if __name__ == "__main__":
    main()