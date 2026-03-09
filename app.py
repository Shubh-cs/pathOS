import streamlit as st
from models import create_tables,add_goal

create_tables()

st.title("PathOS — Execution Engine")

# Expandable Add Goal section
with st.expander("➕ Add Goal"):
    goal_name = st.text_input("Goal Name")

    if st.button("Create Goal"):
        if goal_name:
            add_goal(goal_name)
            st.success(f"Goal '{goal_name}' added successfully!")
        else:
            st.warning("Please enter a goal name.")
