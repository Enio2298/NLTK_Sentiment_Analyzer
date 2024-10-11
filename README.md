# NLTK Sentiment Analyzer

This Streamlit application reads diary entries from text files, analyzes the sentiment of each entry, and visualizes the positivity and negativity trends over time using Plotly.
Features

    Sentiment Analysis: Analyzes the positivity and negativity of each diary entry using the Natural Language Toolkit (NLTK).
    Visualization: Displays trends of positivity and negativity over time using line charts powered by Plotly.
    Streamlit Dashboard: Provides an interactive dashboard to visualize the sentiment trends of your diary entries.

Prerequisites

    Python 3.x installed.
    Install the required Python libraries:

bash

pip install streamlit nltk plotly

    Download the NLTK sentiment analysis lexicon if you haven't already:

python

import nltk
nltk.download('vader_lexicon')

How It Works

    Reading Diary Entries: The application scans a directory called Exercise/ for .txt files that contain diary entries. Each file represents an entry, and its content is analyzed line by line.

    Sentiment Analysis: The sentiment analysis is performed using NLTK's SentimentIntensityAnalyzer, which provides polarity scores for each line (positive, negative, neutral).

    Visualization: The application visualizes the positivity and negativity trends over time using Plotly line charts. The dates are inferred from the filenames of the diary entries.

Project Structure

bash

project-folder/
│
├── Exercise/              # Folder containing diary text files
│   ├── entry1.txt         # Example diary entry
│   ├── entry2.txt         # Another diary entry
│
├── diary_analyzer.py      # Main Python script for the Streamlit app
└── README.md              # This README file

Usage

    Place your diary entries in the Exercise/ folder as .txt files. The filenames should include dates (e.g., 2024-10-04.txt) to accurately reflect the timeline in the visualizations.

    Run the Streamlit app:

bash

streamlit run diary_analyzer.py

    The app will display two line charts:
        Positivity: A trend of the positive sentiment in your diary entries over time.
        Negativity: A trend of the negative sentiment in your diary entries over time.

Example Text Files

Each .txt file should contain one or more lines of text representing a diary entry. Example format for a file:

2024-10-04.txt

css

Today was a great day! I felt so happy and accomplished.
The weather was nice, and I finished all my tasks on time.

Customization

    File Location: If your text files are in a different folder, you can change the folder path in the glob.glob("Exercise/*.txt") line to reflect your directory structure.
    Sentiment Analysis: The current sentiment analysis is line-based. You can modify it to analyze entire entries if needed.
