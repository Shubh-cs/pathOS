import streamlit as st
from models import create_tables

create_tables()

st.title("PathOS — Execution Engine")
st.success("Database initialized successfully.")
