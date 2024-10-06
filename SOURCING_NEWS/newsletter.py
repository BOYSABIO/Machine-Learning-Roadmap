import requests
from bs4 import BeautifulSoup
import openai  # OpenAI GPT library
import datetime

# Set your OpenAI GPT API key
openai.api_key = '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'  # Replace with your actual API key

# Function to fetch news articles from a specific URL within a time period
def fetch_news(url, start_date, end_date):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_articles = soup.find_all('article')  # Adjust based on the HTML structure of the news source
    
    filtered_articles = []
    for article in all_articles:
        # Extract the publication date from the article (this is a hypothetical example, you need to adapt it)
        publication_date_str = article.find('span', class_='publication-date').text
        publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d')

        # Check if the article is within the specified time period
        if start_date <= publication_date <= end_date:
            filtered_articles.append(article.get_text())
    
    return filtered_articles

# Function to interact with ChatGPT for content generation
def generate_content(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # You can use other engines like "text-davinci-003" based on your preference
        prompt=prompt,
        max_tokens=300,  # Adjust as needed
        temperature=0.7,  # Adjust as needed (higher values make output more random)
        n=1,
    )
    return response.choices[0].text.strip()

# Sample list of news sources
news_sources = [
    "https://example.com/news-source-1",
    "https://example.com/news-source-2",
    # Add more news sources as needed
]

# Set the time period for fetching news
start_date = datetime(2023, 1, 1)  # Adjust as needed
end_date = datetime(2023, 12, 31)  # Adjust as needed

# Fetch and summarize news from each source within the specified time period
all_news = []
for source in news_sources:
    articles = fetch_news(source, start_date, end_date)
    for article in articles:
        # Use ChatGPT to generate a summary for each article
        prompt = f"Summarize the following article:\n\n{article}\n\nSummary:"
        summary = generate_content(prompt)
        all_news.append(summary)