import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

genai.configure(api_key="")

def fetch_news_content(url):
    """Scrape article content from a news URL."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        paragraphs = soup.find_all("p")
        article_text = " ".join([para.get_text() for para in paragraphs])
        return article_text[:5000]  # Limit text to avoid exceeding token limits
    except Exception as e:
        return f"Error fetching content: {e}"

def summarize_content(text):
    """Use Gemini to summarize the news article."""
    prompt = f"Summarize the following article in 5 key bullet points:\n\n{text}"
    
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text

def answer_query(text, question):
    """Use Gemini to answer specific questions about the news article."""
    prompt = f"Based on the following article, answer this question:\n\nArticle: {text}\n\nQuestion: {question}"
    
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text

st.set_page_config(page_title="AI News Agent", page_icon="📰", layout="wide")

st.title("📰 AI Research Agent with Gemini 1.5 Flash")
st.write("Paste a news article URL, and let AI summarize and answer your questions!")

news_url = st.text_input("🔗 Enter News/Article/Web page URL", "")

if st.button("Fetch & Summarize"):
    if news_url:
        with st.spinner("Fetching and summarizing..."):
            article_text = fetch_news_content(news_url)
            
            if "Error" in article_text:
                st.error(article_text)
            else:
                summary = summarize_content(article_text)
                st.subheader("🔹 Summary")
                st.write(summary)
                
                st.session_state["article_text"] = article_text  # Store for later use
    else:
        st.warning("Please enter a valid news URL.")

if "article_text" in st.session_state:
    st.subheader("🔍 Ask a Question")
    user_question = st.text_input("Type your question about the article")
    
    if st.button("Get Answer"):
        if user_question:
            with st.spinner("Generating answer..."):
                answer = answer_query(st.session_state["article_text"], user_question)
                st.subheader("💡 Answer")
                st.write(answer)
        else:
            st.warning("Please enter a question.")

