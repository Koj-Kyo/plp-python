# CORD-19 Metadata Analysis and Streamlit App
# -------------------------------------------
# This script demonstrates basic data loading, cleaning, analysis, and visualization
# for the CORD-19 metadata.csv dataset. It also provides a simple Streamlit app
# for interactive exploration.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --- Part 1: Data Loading and Basic Exploration ---

# Load the metadata.csv file (ensure it's in the same directory or provide the path)
try:
    df = pd.read_csv('metadata.csv', low_memory=False)
except FileNotFoundError:
    print("metadata.csv not found. Please download it from Kaggle and place it in this directory.")
    exit()

# Display first few rows and structure
print("First 5 rows:")
print(df.head())
print("\nDataFrame shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values (top 10 columns):")
print(df.isnull().sum().sort_values(ascending=False).head(10))
print("\nBasic statistics for numerical columns:")
print(df.describe())

# --- Part 2: Data Cleaning and Preparation ---

# Handle missing values: drop rows with missing 'publish_time' or 'title'
df_clean = df.dropna(subset=['publish_time', 'title']).copy()

# Convert publish_time to datetime and extract year
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean = df_clean.dropna(subset=['publish_time'])
df_clean['year'] = df_clean['publish_time'].dt.year

# Create abstract word count column
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(x.split()))

# --- Part 3: Data Analysis and Visualization ---

# 1. Count papers by publication year
year_counts = df_clean['year'].value_counts().sort_index()

# 2. Top 10 journals
top_journals = df_clean['journal'].value_counts().head(10)

# 3. Most frequent words in titles (simple frequency)
from collections import Counter
import re
all_titles = ' '.join(df_clean['title'].dropna()).lower()
words = re.findall(r'\b\w+\b', all_titles)
common_words = Counter(words)
common_words = {k: v for k, v in common_words.items() if k not in ['the', 'and', 'of', 'in', 'to', 'a', 'for', 'on', 'with', 'by', 'an', 'at', 'from', 'as', 'is', 'are']}
top_words = dict(Counter(common_words).most_common(20))

# 4. Paper counts by source
source_counts = df_clean['source_x'].value_counts().head(10)

# --- Visualization Section ---

# Publications by Year
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.tight_layout()
plt.savefig('publications_by_year.png')
plt.close()

# Top Journals Bar Chart
plt.figure(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.tight_layout()
plt.savefig('top_journals.png')
plt.close()

# Word Cloud of Titles
try:
    from wordcloud import WordCloud
    wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_words)
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('Most Frequent Words in Paper Titles')
    plt.tight_layout()
    plt.savefig('title_wordcloud.png')
    plt.close()
except ImportError:
    print("wordcloud package not installed. Skipping word cloud.")

# Source Distribution
plt.figure(figsize=(10,5))
sns.barplot(x=source_counts.values, y=source_counts.index, palette='magma')
plt.title('Top 10 Sources')
plt.xlabel('Number of Papers')
plt.ylabel('Source')
plt.tight_layout()
plt.savefig('source_distribution.png')
plt.close()

# --- Part 4: Streamlit Application ---

def run_streamlit_app():
    st.title("CORD-19 Data Explorer")
    st.write("Simple exploration of COVID-19 research papers (metadata.csv)")

    # Year range slider
    min_year, max_year = int(df_clean['year'].min()), int(df_clean['year'].max())
    year_range = st.slider("Select publication year range", min_year, max_year, (min_year, max_year))
    filtered = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]

    st.subheader("Sample Data")
    st.write(filtered[['title', 'journal', 'publish_time', 'authors']].head(10))

    st.subheader("Publications by Year")
    st.image('publications_by_year.png')

    st.subheader("Top 10 Journals")
    st.image('top_journals.png')

    st.subheader("Most Frequent Words in Titles")
    try:
        st.image('title_wordcloud.png')
    except Exception:
        st.write("Word cloud not available.")

    st.subheader("Top 10 Sources")
    st.image('source_distribution.png')

    st.write("Data source: CORD-19 metadata.csv")

# To run the Streamlit app, use: streamlit run libr.py

if __name__ == "__main__":
    # Uncomment the next line to run the Streamlit app directly
    # run_streamlit_app()
    print("Script executed. Visualizations saved as PNG files. To launch the Streamlit app, run:\nstreamlit run libr.py")
