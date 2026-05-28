import streamlit as st
from agents.travel_agent import agent

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🧳✈️🕶️",
    layout="wide"
)
st.title("✈️ Agentic AI Travel Planning Assistant")
st.write("🕵️‍♂️🗺️💻 Plan your trips using Langchain + LLM + Agentic AI")
query = st.text_area("Enter your travel query here (e.g., 'Plan a trip from delhi to goa with hotels ,flight and weather info')")
if st.button("Plan My Trip"):
    if query:
        with st.spinner("Planning your trip..."):
            try:
                response = agent(query)
                st.success("Travel plan is ready!")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query to plan your trip.")