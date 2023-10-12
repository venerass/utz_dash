import pandas as pd
import numpy as np
import streamlit as st

import time
import datetime

import plotly.express as px


st.set_page_config(page_title='Longevidade de empresas familiares', 
                   page_icon='./usage/data/images/logo_UTZ_branco.png',
                   initial_sidebar_state='collapsed',
                   layout='wide')

# with st.sidebar:
#     st.image('usage/data/images/logo_cinnecta.png',width=200)

col1, col2 = st.columns(spec=[0.8,0.2],gap='small')
with col1:
    st.markdown('# Longevidade de empresas familiares')

with col2:
    st.markdown('###')
    st.image('./usage/data/images/logo_UTZ_verde.png',width=230)


st.markdown('#')

# Define the questions
questions = {
    "Coesão Familiar": [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5",
        "Question 6",
        "Question 7",
        "Question 8",
        "Question 9",
        "Question 10",
        "Question 11"
    ],
    "Governança Familiar": [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5",
        "Question 6",
        "Question 7",
        "Question 8",
        "Question 9",
        "Question 10",
        "Question 11",
        "Question 12",
        "Question 13",
        "Question 14",
        "Question 15",
        "Question 16",
        "Question 17",
        "Question 18"
    ],
    "Familiares preparados e Contributivos": [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5",
        "Question 6",
        "Question 7",
        "Question 8",
        "Question 9",
        "Question 10"
    ],
    "Governança Corporativa": [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5",
        "Question 6",
        "Question 7",
        "Question 8",
        "Question 9",
        "Question 10",
        "Question 11",
        "Question 12",
        "Question 13",
        "Question 14",
        "Question 15",
        "Question 16",
        "Question 17",
        "Question 18",
        "Question 19"
    ],
    "Gestão Eficaz": [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5",
        "Question 6",
        "Question 7",
        "Question 8",
        "Question 9",
        "Question 10",
        "Question 11",
        "Question 12",
        "Question 13",
        "Question 14"
    ]
}

# Define the possible answers and their corresponding points
answers = {
    "Discordo totalmente": 1,
    "Discordo parcialmente": 2,
    "Não concordo, nem discordo": 3,
    "Concordo parcialmente": 4,
    "Concordo plenamente": 5
}

# Define the number of questions for each main topic
num_questions = {
    "Coesão Familiar": 11,
    "Governança Familiar": 18,
    "Familiares preparados e Contributivos": 10,
    "Governança Corporativa": 19,
    "Gestão Eficaz": 14
}

# Create a form-like stream of questions
st.markdown("# Responda as perguntas abaixo:")
points = {}
for topic, num in num_questions.items():
    with st.container():
        st.markdown(f"## {topic}")
        topic_points = []
        for i in range(num):
            question = questions[topic][i]
            # answer = st.radio(question, answers.keys(), key=f"{topic}-{i}")
            answer = st.select_slider(question, answers.keys(), key=f"{topic}-{i}")
            topic_points.append(answers[answer])
        points[topic] = topic_points

# Calculate the total points for each main topic
total_points = {}
for topic, topic_points in points.items():
    total_points[topic] = sum(topic_points)

# Create a spider graph to visualize the total points for each main topic
df = pd.DataFrame({
    "Main Topic": list(total_points.keys()),
    "Total Points": list(total_points.values())
})
fig = px.line_polar(df, r="Total Points", theta="Main Topic", line_close=True)
st.plotly_chart(fig)


