import glob
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer as analyzer
import plotly.express as px

sia = analyzer()


def get_data():
    fechas = []
    p = []
    n = []
    files = glob.glob("Exercise/*.txt")

    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                scores = sia.polarity_scores(line)
            p.append(scores["pos"])
            n.append(scores["neg"])
            fechas.append(file)
    return p, n, fechas


p, n, dates = get_data()

dates = [name.strip(".txt").strip("Exercise\\") for name in dates]

st.title("Diary Tone")

st.subheader("Positivity")
figure = px.line(x=dates, y=p,
                 labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figure)
st.subheader("Negativity")
figure1 = px.line(x=dates, y=n,
                  labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(figure1)
