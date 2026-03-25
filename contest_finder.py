import streamlit as st
import pandas as pd

# -----------------------
# Contest Data
# -----------------------
# Each contest: (Name, Description, URL)
contests = [
    ("RW&CO Canada Contest", "Win a $100 Gift Card for Spring!", "https://www.canadianfreestuff.com/rwco-canada-contest/"),
    ("Costco Canada Contest", "Win 1 of two $100 Gift Cards!", "https://www.canadianfreestuff.com/costco-canada-contest/"),
    ("Best Buy Canada", "Win a $2500 Gift Card in the 25th Anniversary Contest!", "https://www.canadianfreestuff.com/best-buy-canada-contest/"),
    ("Huggies Canada Contest", "Win a 6-mo supply of Diapers & Wipes + $500 Amazon gift card!", "https://www.canadianfreestuff.com/huggies-canada-contest/"),
    ("Linen Chest Canada Contest", "Win a Mushroom Lamp OR a $1000 Linen Chest Gift Card", "https://www.canadianfreestuff.com/linen-chest-canada-contest/"),
    ("Milestones Canada Contest", "Win a $50 Gift Card + Free Appy & Free Birthday Dessert!", "https://www.canadianfreestuff.com/milestones-canada-free-sample/"),
    ("Home Depot Canada Contest", "Win a $1000 Home Depot Gift Card from Behr", "https://www.canadianfreestuff.com/home-depot-canada-contest/"),
    ("HomeSense Canada Contest", "Win 1 of FOUR $250 Homesense or Marshalls Gift Cards", "https://www.canadianfreestuff.com/homesense-contest/"),
    ("Nerds Gummy Clusters Canada", "Win a Trip for 2 to PARIS + INSTANT WIN!", "https://www.canadianfreestuff.com/nerds-canada-contest/"),
    ("Budweiser Canada Contest", "Win a Trip to the 2026 Stanley Cup Final", "https://www.canadianfreestuff.com/budweiser-canada-contest/"),
    ("Visa Contest Canada", "Win a $150 or $250 Visa Gift Card", "https://www.canadianfreestuff.com/visa-contest-win-visa-gift-card-canada/"),
    ("Dole Contest Canada", "Win a Vacation for 2 to Hawaii!", "https://www.canadianfreestuff.com/dole-canada-contest/"),
    ("Old Dutch Discover Canada Contest", "Win $2,000 Cash, $500 gift card, and more", "https://www.canadianfreestuff.com/old-dutch-canada-contest/"),
    ("Sleep Country Contest", "Win a $700 Sleep Country Canada Bedding Bundle", "https://www.canadianfreestuff.com/sleep-country-contest/"),
    ("Parents Canada Contest", "Win $500 in cold, hard CASH!", "https://www.canadianfreestuff.com/parents-canada-contests/"),
    ("Canadian Woodworking Contest", "Win a $500 Whisky Jack Hand Tool Package", "https://www.canadianfreestuff.com/canadian-woodworking-contest/"),
    # ... you can continue adding all contests here ...
]

# -----------------------
# Remove duplicates
# -----------------------
seen = set()
unique_contests = []
for name, desc, url in contests:
    if name not in seen:
        unique_contests.append((name, desc, url))
        seen.add(name)

# -----------------------
# Streamlit App
# -----------------------
st.set_page_config(page_title="Canadian Contest Finder", layout="wide")
st.title("🎯 Canadian Contest Finder")

st.markdown(f"Found **{len(unique_contests)}** Canadian contests:")

for name, desc, url in unique_contests:
    st.markdown(f"- [{name}]({url})  \n{desc}")

st.caption("Data compiled from Canadian freebie and contest sites.")