import streamlit as st

# --- FULL DATA LIST ---
data = [
    # ... paste the full contest data I gave you in the last message ...
]

st.title("🎯 Canadian Contest Finder")
st.write(f"Found {len(data)} Canadian contests:")

# Optional: sort by priority (highest first)
data_sorted = sorted(data, key=lambda x: x.get("priority", 0), reverse=True)

# Display all contests
for contest in data_sorted:
    st.markdown(f"**• [{contest['name']}]({contest['url']})**")
    st.markdown(f"{contest['description']}")
    st.markdown(f"*Priority: {contest['priority']}*")
    st.markdown("---")