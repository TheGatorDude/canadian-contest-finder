import requests
from datetime import datetime
import os

# Output file
OUTPUT_FILE = "canada_contests_all_sites.txt"
# Keep a set of existing URLs to avoid duplicates
existing_urls = set()

# Load existing URLs if the file exists
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("http"):
                existing_urls.add(line)

# Sites to scrape
SITES = [
    "https://www.canadianfreestuff.com/canadian-contests/",
    "https://www.contestscoop.com/canadian-contests/",
    "https://www.sweepstakes.ca/",
    # Add more sources if desired
]

# Words to ignore
BAD_KEYWORDS = [
    "coupon", "coupons", "free samples", "magazine",
    "browse", "category", "facebook contests",
    "freebies", "print", "mail", "signup",
    # Meta pages we want to ignore
    "popular page", "latest canadian contests",
    "trusted contest & giveaway directory",
    "enter daily contests"
]

# Function to score contests by prize value
def score_contest(title):
    title = title.lower()
    score = 0
    if "$" in title:
        score += 3
    if "win" in title:
        score += 2
    if "trip" in title or "vacation" in title:
        score += 5
    if "gift card" in title:
        score += 2
    if "iphone" in title or "macbook" in title or "samsung" in title:
        score += 4
    if "cash" in title or "money" in title:
        score += 5
    if "luxury" in title or "expensive" in title:
        score += 3
    return score

# Collect contests
contests = []

for site in SITES:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(site, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch {site}")
            continue

        # Very simple scraping: look for <a href=""> links
        links = response.text.split("<a ")
        for link in links[1:]:
            if "href=" not in link:
                continue
            parts = link.split("href=")
            url_part = parts[1].split(">")[0].strip(' "\'')
            text_part = parts[1].split(">")[1].split("<")[0].strip()

            if not url_part.lower().startswith("http"):
                continue
            if any(bad in text_part.lower() for bad in BAD_KEYWORDS):
                continue
            if "canada" not in text_part.lower():
                continue
            if url_part in existing_urls:
                continue

            contests.append((text_part, url_part))
            existing_urls.add(url_part)
    except Exception as e:
        print(f"Error fetching {site}: {e}")

# Sort by prize score
contests.sort(key=lambda x: score_contest(x[0]), reverse=True)

# Append to output file
with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    f.write(f"\n🎯 Found {len(contests)} new contests ({datetime.now().strftime('%Y-%m-%d')}):\n\n")
    for title, url in contests:
        f.write(f"• [{url}] {title}\n   {url}\n\n")

print(f"💾 Saved {len(contests)} new contests to {OUTPUT_FILE}")