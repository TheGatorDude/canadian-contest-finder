import streamlit as st
import pandas as pd

# -----------------------------
# Sample contest data
# -----------------------------
data = [
    {
        "name": "RW&CO Canada Contest",
        "description": "Win a $100 Gift Card for Spring!",
        "url": "https://www.canadianfreestuff.com/rwco-canada-contest/",
        "priority": 2,
        "category": "Shopping"
    },
    {
        "name": "Budweiser Canada Contest",
        "description": "Win a Trip to the 2026 Stanley Cup Final",
        "url": "https://www.canadianfreestuff.com/budweiser-canada-contest/",
        "priority": 5,
        "category": "Travel"
    },
    {
        "name": "Apple iPhone Contest Canada",
        "description": "Win a New Apple Watch Series 11",
        "url": "https://www.canadianfreestuff.com/apple-canada-contest/",
        "priority": 4,
        "category": "Electronics"
    },
    # Add more contests here...
]

# Convert to DataFrame
df = pd.DataFrame(data)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filter Contests")

# Search box (optional)
search = st.sidebar.text_input("Search contests (name or description)")

# Priority filter
priority_filter = st.sidebar.slider("Minimum Priority", min_value=1, max_value=5, value=1)

# Category filter (optional)
categories = list(df['category'].unique())
category_filter = st.sidebar.multiselect("Categories", categories, default=categories)

# -----------------------------
# Filtering logic
# -----------------------------
filtered_df = df.copy()

# Filter by search term if provided
if search:
    filtered_df = filtered_df[
        filtered_df['name'].str.contains(search, case=False) |
        filtered_df['description'].str.contains(search, case=False)
    ]

# Filter by priority
filtered_df = filtered_df[filtered_df['priority'] >= priority_filter]

# Filter by category (only if selected)
if category_filter:
    filtered_df = filtered_df[filtered_df['category'].isin(category_filter)]

# -----------------------------
# Display contests
# -----------------------------
st.title("🎯 Canadian Contest Finder")
st.write(f"Found {len(filtered_df)} contests:")

for _, row in filtered_df.iterrows():
    st.markdown(f"• [{row['name']}]({row['url']})  \n{row['description']}  \nPriority: {row['priority']}")