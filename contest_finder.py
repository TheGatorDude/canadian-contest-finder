import streamlit as st
import pandas as pd

# --- Example data ---
contests = [
    {"name": "RW&CO Canada Contest", "description": "Win a $100 Gift Card for Spring!", "url": "https://www.canadianfreestuff.com/rwco-canada-contest/", "category": "Gift Card", "priority": 2},
    {"name": "Budweiser Canada Contest", "description": "Win a Trip to the 2026 Stanley Cup Final", "url": "https://www.canadianfreestuff.com/budweiser-canada-contest/", "category": "Travel", "priority": 5},
    {"name": "Apple iPhone Contest Canada", "description": "Win a New Apple Watch Series 11", "url": "https://www.canadianfreestuff.com/apple-canada-contest/", "category": "Electronics", "priority": 4},
    # ... add all your contests here
]

df = pd.DataFrame(contests)

st.title("🎯 Canadian Contest Finder")
st.markdown("Find the best Canadian contests with links, descriptions, and priority scores!")

# --- Filters ---
search = st.text_input("Search contests (keywords):")
category_filter = st.multiselect("Filter by category:", options=df['category'].unique(), default=df['category'].unique())
priority_filter = st.slider("Minimum priority:", 1, 5, 1)

# --- Filter dataframe ---
filtered_df = df[
    df['name'].str.contains(search, case=False) &
    df['category'].isin(category_filter) &
    (df['priority'] >= priority_filter)
]

# --- Optional refresh button ---
if st.button("🔄 Refresh Data"):
    st.info("Refreshing data... (for now this just reloads the static list)")
    # Here you could call your scraping function to update df

# --- Display contests ---
for _, row in filtered_df.iterrows():
    st.markdown(f"• [{row['name']}]({row['url']})  \n{row['description']}  \nPriority: {row['priority']}")

# --- Optional: show total count ---
st.markdown(f"**Total contests shown:** {len(filtered_df)}")