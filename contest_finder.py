# contest_finder.py
import streamlit as st

st.title("🎯 Canadian Contest Finder")

# Full list of 57 contests with name and URL
contests = [
    ("RW&CO Canada Contest", "https://www.canadianfreestuff.com/rwco-canada-contest/"),
    ("Costco Canada Contest", "https://www.canadianfreestuff.com/costco-canada-contest/"),
    ("Best Buy Canada Contest", "https://www.canadianfreestuff.com/best-buy-canada-contest/"),
    ("Huggies Canada Contest", "https://www.canadianfreestuff.com/huggies-canada-contest/"),
    ("Linen Chest Canada Contest", "https://www.canadianfreestuff.com/linen-chest-canada-contest/"),
    ("Milestones Canada Contest", "https://www.canadianfreestuff.com/milestones-canada-free-sample/"),
    ("Home Depot Canada Contest", "https://www.canadianfreestuff.com/home-depot-canada-contest/"),
    ("HomeSense Canada Contest", "https://www.canadianfreestuff.com/homesense-contest/"),
    ("Nerds Gummy Clusters Canada Contest", "https://www.canadianfreestuff.com/nerds-canada-contest/"),
    ("Budweiser Canada Contest", "https://www.canadianfreestuff.com/budweiser-canada-contest/"),
    ("Visa Contest Canada", "https://www.canadianfreestuff.com/visa-contest-win-visa-gift-card-canada/"),
    ("Dole Contest Canada", "https://www.canadianfreestuff.com/dole-canada-contest/"),
    ("Old Dutch Discover Canada Contest", "https://www.contestscoop.com/old-dutch-canada-contest/"),
    ("Sleep Country Contest", "https://www.canadianfreestuff.com/sleep-country-contest/"),
    ("Parents Canada Contest", "https://www.canadianfreestuff.com/parents-canada-contests/"),
    ("Old Dutch Discover Canada Contest 2", "https://www.canadianfreestuff.com/old-dutch-canada-contest/"),
    ("Canadian Woodworking Contest", "https://www.canadianfreestuff.com/canadian-woodworking-contest/"),
    ("Avon Canada Contest", "https://www.canadianfreestuff.com/avon-canada-contest/"),
    ("Air Miles Canada Contest", "https://www.canadianfreestuff.com/air-miles-canada-contest/"),
    ("Molson Canadian Contest", "https://www.canadianfreestuff.com/molson-canadian-contest/"),
    ("Glad Canada Contest Instagram", "https://www.contestscoop.com/glad-canada-contest/"),
    ("Glad Canada Contest Instagram/Facebook", "https://www.contestscoop.com/glad-canada-contest/"),
    ("Canada's Luckiest Family Contest", "https://www.contestscoop.com/canadas-luckiest-family-contest/"),
    ("Clearly Canadian Contest", "https://www.canadianfreestuff.com/clearly-canadian-contest/"),
    ("Staples Canada Contest", "https://www.canadianfreestuff.com/staples-canada-contest/"),
    ("Android Contest Canada", "https://www.canadianfreestuff.com/android-canada-contest/"),
    ("Apple iPhone Contest Canada", "https://www.canadianfreestuff.com/apple-canada-contest/"),
    ("Aeroplan Canada Contest", "https://www.canadianfreestuff.com/aeroplan-canada-contest/"),
    ("Cineplex Canada Contest", "https://www.canadianfreestuff.com/cineplex-canada-contest/"),
    ("Philips Canada Contest", "https://www.canadianfreestuff.com/philips-canada-contest/"),
    ("Kubota Canada BX Summer Contest", "https://www.canadianfreestuff.com/kubota-contest/"),
    ("Cub Cadet Contest", "https://www.canadianfreestuff.com/cub-cadet-canada-contest/"),
    ("Parent Life Network Contest", "https://www.canadianfreestuff.com/canada-luckiest-family-contest/"),
    ("Kinder Contest Canada", "https://www.canadianfreestuff.com/kinder-canada-contests/"),
    ("Conair Contest Canada", "https://www.canadianfreestuff.com/conair-canada-contest/"),
    ("Mr. Lube Canada Contest", "https://www.canadianfreestuff.com/mr-lube-canada-contest/"),
    ("Playstation Canada Contest", "https://www.canadianfreestuff.com/playstation-canada-contest/"),
    ("Team Canada Contest", "https://www.canadianfreestuff.com/team-canada-contest/"),
    ("Napoleon BBQ Canada Contest", "https://www.canadianfreestuff.com/napoleon-canada-contest/"),
    ("Lindt Canada Easter Contest", "https://www.canadianfreestuff.com/lindt-canada-contest/"),
    ("Telus Canada Contest", "https://www.canadianfreestuff.com/telus-canada-contest/"),
    ("Rogers Canada Contest", "https://www.canadianfreestuff.com/rogers-canada-contest/"),
    ("Aero Canada Contest", "https://www.canadianfreestuff.com/aero-canada-contest/"),
    ("Scotties Contest Canada", "https://www.canadianfreestuff.com/scotties-canada-contest/"),
    ("Dove Canada Contest", "https://www.canadianfreestuff.com/dove-canada-contest/"),
    ("Fish’n Canada Contest", "https://www.canadianfreestuff.com/fish-n-canada-contest/"),
    ("Tribute Contest Canada", "https://www.canadianfreestuff.com/tribute-canada-contest/"),
    ("Orange Naturals Canada Contest", "https://www.canadianfreestuff.com/orange-naturals-magpop-free-sample/"),
    ("Canada Dry Contest", "https://www.canadianfreestuff.com/canada-dry-contest/"),
    ("Contest Scoop Canadian Contests", "https://www.contestscoop.com/canadian-contests/"),
    ("Latest Canadian contests", "https://www.contestscoop.com/canadian-contests/"),
    ("Popular Page Canada Contests", "https://www.contestscoop.com/canadian-contests/"),
    ("Facebook Canada Contests", "https://www.contestscoop.com/facebook-contests/"),
    ("Contest Scoop Directory", "https://www.contestscoop.com/"),
    ("Canada Contests", "https://www.canadianfreestuff.com/canadian-contests/"),
    ("Enter Daily Contests Canada", "https://www.canadianfreestuff.com/canadian-contests/enter-daily/"),
]

st.write(f"Found {len(contests)} Canadian contests:")

# Show contests as clickable links
for name, url in contests:
    st.markdown(f"• [{name}]({url})")