import streamlit as st
from models import create_tables,add_goal,get_goals,add_event,get_events

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

st.subheader("Current Goals")

goals = get_goals()

if goals:
    for goal in goals:
        with st.expander(f"🎯 {goal['name']}"):

            # Add Event Form
            event_name = st.text_input(
                "Event Name",
                key=f"event_name_{goal['id']}"
            )

            event_category = st.selectbox(
                "Category",
                ["Internship", "Hackathon", "Competition", "College", "Personal"],
                key=f"category_{goal['id']}"
            )

            event_deadline = st.date_input(
                "Deadline",
                key=f"deadline_{goal['id']}"
            )

            if st.button("Add Event", key=f"add_event_{goal['id']}"):
                if event_name:
                    add_event(event_name, event_deadline, event_category, goal["id"])
                    st.success("Event added successfully!")
                else:
                    st.warning("Please enter an event name.")

            # Show existing events
            events = get_events(goal["id"])

            if events:
                st.write("Events:")
                for event in events:
                    st.write(f"📌 {event['name']} ({event['category']})")
            else:
                st.info("No events added yet.")

else:
    st.info("No goals added yet.")