import streamlit as st

# Define the pages 
main_page = st.Page("main_page.py", title = "Main Page")
second_page = st.Page("first_plan.py", title = "Plan 1")
third_page = st.Page("second_plan.py", title = "Plan 2")

# Set up navigation
pg = st.navigation([main_page, second_page, third_page])

# Run the selected pages
pg.run()