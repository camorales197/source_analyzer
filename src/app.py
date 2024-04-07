import streamlit as st
import pandas as pd
import time

def load_articles():
    """
    Load articles from a CSV file.

    Returns:
        DataFrame: A DataFrame containing the articles.
    """
    path = "/Users/carlosmorales/Desktop/Carlos/personal_projects/afganistan_news/results/final_results.csv"
    return pd.read_csv(path)

def filter_articles_by_conflict(articles, conflict):
    """
    Filter articles by conflict.

    Args:
        articles (DataFrame): The DataFrame containing the articles.
        conflict (str): The conflict to filter by.

    Returns:
        DataFrame: A DataFrame containing the filtered articles.
    """
    return articles[articles['topic'] == conflict]

def source_analyzer():
    """
    Function for the Source Analyzer tab.
    """
    st.header('Source Origin Detection and Bias Analysis')
    articles = load_articles()

    with st.form("analysis_form"):
        conflict_query = st.selectbox('Select the conflict you are interested in:',
                                      ['Ukraine'])
        submit_button = st.form_submit_button('Analyze')

    if submit_button:
        with st.spinner('Analyzing...'):
            filtered_articles = filter_articles_by_conflict(articles, 'Ukraine')
            time.sleep(5)
            st.success('Analysis complete!')
            st.write('Analysis of sources:')
            st.dataframe(filtered_articles)

def find_articles():
    """
    Function for the Find Articles tab.
    """
    st.header('Find Articles with Prominent Sources')

    with st.form("find_articles_form"):
        source_preference = st.selectbox('Select the source side you wish to see more represented:',
                                         ['US-based', 'Local', 'International', 'Other'])
        submit_button = st.form_submit_button('Find Articles')

    if submit_button:
        with st.spinner('Searching for articles...'):
            articles = load_articles()
            filtered_articles = filter_articles_by_conflict(articles, 'Ukraine')
            st.success('Found articles!')
            st.write('Articles where the selected source side is more represented will be listed here.')
            st.dataframe(filtered_articles)

def main():
    st.title('Conflict News Analysis Tool')
    st.write('This tool helps detect and analyze the sources cited in news articles related to conflicts, \
             to determine potential biases based on the origin of these sources.')

    tab1, tab2 = st.tabs(["Source Analyzer", "Find Articles"])

    with tab1:
        source_analyzer()

    with tab2:
        find_articles()

if __name__ == '__main__':
    main()


