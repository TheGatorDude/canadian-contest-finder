import streamlit as st

st.set_page_config(page_title="Canadian Contest Finder", layout="wide")

# You had the contest data hardcoded or in a text file
contests = [
    {
        "name": "RW&CO Canada Contest",
        "description": "Win a $100 Gift Card for Spring!",
        "url": "https://www.canadianfreestuff.com/rwco-canada-contest/"
    },
    {
        "name": "Costco Canada Contest",
        "description": "Win 1 of two $100 Gift Cards!",
        "url": "https://www.canadianfreestuff.com/costco-canada-contest/"
    },
    {
        "name": "Best Buy Canada",
        "description": "Win a $2500 Gift Card in the 25th Anniversary Contest!",
        "url": "https://www.canadianfreestuff.com/best-buy-canada-contest/"
    },
    {
        "name": "Huggies Canada Contest",
        "description": "Win a 6-mo supply of Diapers & Wipes + $500 Amazon gift card!",
        "url": "https://www.canadianfreestuff.com/huggies-canada-contest/"
    },
    # …add all 50+ contests here
]

st.title("🎯 Canadian Contest Finder")
st.write(f"Found {len(contests)} Canadian contests:")

for c in contests:
    st.markdown(f"• [{c['name']}]({c['url']})  \n{c['description']}")