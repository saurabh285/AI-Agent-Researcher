# 📰 AI Research Agent using Gemini 1.5 Flash

This is an **AI-Agent research assistant** that fetches news articles, **summarizes key points**, and **answers user queries** using **Gemini 1.5 Flash**.

## 🚀 Features
- **Fetches News Articles** from a provided URL.
- **Summarizes Content** into concise bullet points.
- **Answers Questions** based on the article.
- **Uses Streamlit for UI** with a simple and interactive interface.
- **Secure API Key Management** using `st.secrets` in Streamlit Cloud.

---



## 📜 Usage Instructions
1. **Enter a News URL** in the input box.
2. Click **"Fetch & Summarize"** to get key bullet points.
3. **Ask questions** about the article, and get AI-Agent's responses.

---

## 🔧 Troubleshooting

### **❌ Error: "Read timed out"**
✔ **Fix:** Increase timeout in `fetch_news_content()`
```python
response = requests.get(url, timeout=30)
```

### **❌ Error: "Could not extract meaningful content"**
✔ **Fix:** Use `trafilatura` for better text extraction instead of `newspaper3k`.
```bash
pip install trafilatura
```
**Updated Code for Reliable News Extraction:**
```python
import trafilatura

def fetch_news_content(url):
    """Extracts article content using trafilatura for better reliability."""
    try:
        downloaded = trafilatura.fetch_url(url)
        article_text = trafilatura.extract(downloaded)
        if not article_text:
            return "Error: Unable to extract content from the page."
        return article_text[:5000]  # Limit text length
    except Exception as e:
        return f"Error: {e}"
```




---

## 🏗️ Future Improvements
✅ **Multi-document summarization**  
✅ **AI-powered fact-checking**  
✅ **Memory-based chatbot feature**  

📌 **Contributions are welcome!** Feel free to fork and submit pull requests. 🚀

---

## 💡 Acknowledgments
- **Google AI** for `Gemini 1.5 Flash`
- **Streamlit** for UI
- **trafilatura** for news extraction
- **BeautifulSoup & Requests** (backup method for web scraping)

📌 **Author:** [Saurabh Singh]([https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/saurabh-singh-0528/))

🔗 **Live Demo:** [Streamlit Cloud Link](https://ai-agent-researcher.streamlit.app/)

---

🛠 **Built with ❤️ using AI**

