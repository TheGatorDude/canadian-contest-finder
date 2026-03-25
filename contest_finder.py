import streamlit as st

st.title("🎯 Canadian Contest Finder")

# Full contest list: (Name, URL, Description / Prize)
contests = [
    ("RW&CO Canada Contest", "https://www.canadianfreestuff.com/rwco-canada-contest/", "Win a $100 Gift Card for Spring!"),
    ("Costco Canada Contest", "https://www.canadianfreestuff.com/costco-canada-contest/", "Win 1 of two $100 Gift Cards!"),
    ("Best Buy Canada Contest", "https://www.canadianfreestuff.com/best-buy-canada-contest/", "Win a $2500 Gift Card in the 25th Anniversary Contest!"),
    ("Huggies Canada Contest", "https://www.canadianfreestuff.com/huggies-canada-contest/", "Win a 6-mo supply of Diapers & Wipes + $500 Amazon gift card!"),
    ("Linen Chest Canada Contest", "https://www.canadianfreestuff.com/linen-chest-canada-contest/", "Win a Mushroom Lamp OR a $1000 Linen Chest Gift Card"),
    ("Milestones Canada Contest", "https://www.canadianfreestuff.com/milestones-canada-free-sample/", "Win a $50 Gift Card + Free Appy & Free Birthday Dessert!"),
    ("Home Depot Canada Contest", "https://www.canadianfreestuff.com/home-depot-canada-contest/", "Win a $1000 Home Depot Gift Card from Behr"),
    ("HomeSense Canada Contest", "https://www.canadianfreestuff.com/homesense-contest/", "Win 1 of FOUR $250 Homesense or Marshalls Gift Cards"),
    ("Nerds Gummy Clusters Canada Contest", "https://www.canadianfreestuff.com/nerds-canada-contest/", "Win a Trip for 2 to PARIS + INSTANT WIN!"),
    ("Budweiser Canada Contest", "https://www.canadianfreestuff.com/budweiser-canada-contest/", "Win a Trip to the 2026 Stanley Cup Final"),
    ("Visa Contest Canada", "https://www.canadianfreestuff.com/visa-contest-win-visa-gift-card-canada/", "Win a $150 or $250 Visa Gift Card"),
    ("Dole Contest Canada", "https://www.canadianfreestuff.com/dole-canada-contest/", "Win a Vacation for 2 to Hawaii!"),
    ("Old Dutch Discover Canada Contest", "https://www.contestscoop.com/old-dutch-canada-contest/", "Win $2,000 Cash, $500 gift card, and more"),
    ("Sleep Country Contest", "https://www.canadianfreestuff.com/sleep-country-contest/", "Win a $700 Sleep Country Canada Bedding Bundle"),
    ("Parents Canada Contest", "https://www.canadianfreestuff.com/parents-canada-contests/", "Win $500 in cold, hard CASH!"),
    ("Old Dutch Discover Canada Contest 2", "https://www.canadianfreestuff.com/old-dutch-canada-contest/", "Win 1 of 5 $2,500 prize packs! Plus, 100+ secondary prizes"),
    ("Canadian Woodworking Contest", "https://www.canadianfreestuff.com/canadian-woodworking-contest/", "Win a $500 Whisky Jack Hand Tool Package"),
    ("Avon Canada Contest", "https://www.canadianfreestuff.com/avon-canada-contest/", "Win a $840 Spring Beauty Refresh Prize!"),
    ("Air Miles Canada Contest", "https://www.canadianfreestuff.com/air-miles-canada-contest/", "Win a Shark/Ninja Prize Bundle valued over $10,000!"),
    ("Molson Canadian Contest", "https://www.canadianfreestuff.com/molson-canadian-contest/", "Win Weekly Sporting Goods gift cards, Molson prizes, or a Molson Hockey Experience!"),
    ("Glad Canada Contest", "https://www.contestscoop.com/glad-canada-contest/", "Win Scented Spring Bundle – Instagram & Facebook"),
    ("Canada's Luckiest Family Contest", "https://www.contestscoop.com/canadas-luckiest-family-contest/", "Win Free Rent, Mortgage, RESP, and more"),
    ("Clearly Canadian Contest", "https://www.canadianfreestuff.com/clearly-canadian-contest/", "Win a Stash of Clearly Canadian Cans & Bottles! (NEW)"),
    ("Staples Canada Contest", "https://www.canadianfreestuff.com/staples-canada-contest/", "Win a Logitech MX Master 4 Wireless Mouse"),
    ("Android Contest Canada", "https://www.canadianfreestuff.com/android-canada-contest/", "Win a KingKong X Pro Smartphone, Smartwatch, or Tablet"),
    ("Apple iPhone Contest Canada", "https://www.canadianfreestuff.com/apple-canada-contest/", "Win a New Apple Watch Series 11"),
    ("Aeroplan Canada Contest", "https://www.canadianfreestuff.com/aeroplan-canada-contest/", "Win 25,000 Aeroplan Points and merchandise!"),
    ("Cineplex Canada Contest", "https://www.canadianfreestuff.com/cineplex-canada-contest/", "Win a Project Hail Mary Prize / FREE CineClub Membership & More!"),
    ("Philips Canada Contest", "https://www.canadianfreestuff.com/philips-canada-contest/", "Win a Philips 3300 LatteGo Super Automatic Espresso Machine"),
    ("Kubota Canada BX Summer Contest", "https://www.canadianfreestuff.com/kubota-contest/", "Win 3 months with a Kubota Tractor!"),
    ("Cub Cadet Contest", "https://www.canadianfreestuff.com/cub-cadet-canada-contest/", "Win a VIP Experience to the 2026 RBC Canadian Open"),
    ("Parent Life Network Contest", "https://www.canadianfreestuff.com/canada-luckiest-family-contest/", "Win FREE Rent or Mortgage for a Year!"),
    ("Kinder Contest Canada", "https://www.canadianfreestuff.com/kinder-canada-contests/", "Win a KINDER® Easter prize pack!"),
    ("Conair Contest Canada", "https://www.canadianfreestuff.com/conair-canada-contest/", "Win a Conair x Scunci Luxe Lucky Giveaway"),
    ("Mr. Lube Canada Contest", "https://www.canadianfreestuff.com/mr-lube-canada-contest/", "Win a 6-piece luggage set!"),
    ("Playstation Canada Contest", "https://www.canadianfreestuff.com/playstation-canada-contest/", "Win a Sony 65″ 4K Smart Google TV and a PlayStation5 Console!"),
    ("Team Canada Contest", "https://www.canadianfreestuff.com/team-canada-contest/", "Win a Signed Team Canada Jacket by Bronze Medallists"),
    ("Napoleon BBQ Canada Contest", "https://www.canadianfreestuff.com/napoleon-canada-contest/", "Win 50 Prizes for 50 Years Giveaway!"),
    ("Lindt Canada Easter Contest", "https://www.canadianfreestuff.com/lindt-canada-contest/", "Win a YEAR’S SUPPLY of LINDT CHOCOLATE!"),
    ("Telus Canada Contest", "https://www.canadianfreestuff.com/telus-canada-contest/", "Win the NEW Samsung Galaxy S26 Ultra!"),
    ("Rogers Canada Contest", "https://www.canadianfreestuff.com/rogers-canada-contest/", "Win the NEW Samsung Galaxy S26 Ultra /NHL Tickets & Jerseys"),
    ("Aero Canada Contest", "https://www.canadianfreestuff.com/aero-canada-contest/", "Win 1 of 2 Mind Bubbling VIP PWHL experiences!"),
    ("Scotties Contest Canada", "https://www.canadianfreestuff.com/scotties-canada-contest/", "Win a 1-Year Supply of Kruger Products"),
    ("Dove Canada Contest", "https://www.canadianfreestuff.com/dove-canada-contest/", "WIN an EA SPORTS FC 26 in-game Ultimate Team pack"),
    ("Fish’n Canada Contest", "https://www.canadianfreestuff.com/fish-n-canada-contest/", "Win a Garmin LiveScope XR System!"),
    ("Tribute Contest Canada", "https://www.canadianfreestuff.com/tribute-canada-contest/", "Win a ZOOTOPIA 2 Combo Pack"),
    ("Orange Naturals Canada Contest", "https://www.canadianfreestuff.com/orange-naturals-magpop-free-sample/", "Win a Box of MagPop!"),
    ("Canada Dry Contest", "https://www.canadianfreestuff.com/canada-dry-contest/", "Win 1 of 3 Blue Jays VIP Experiences + 100’s of prizes to be won!"),
]

st.write(f"Found {len(contests)} Canadian contests:")

# Display contests with description/prize
for name, url, desc in contests:
    st.markdown(f"• [{name}]({url})  \n  *{desc}*")