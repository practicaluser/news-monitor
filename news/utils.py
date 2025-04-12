import requests
from bs4 import BeautifulSoup

def crawl_naver_news(keyword, max_articles=5):
    url = f"https://search.naver.com/search.naver?where=news&query={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    articles = soup.select('ul.list_news div.news_wrap.api_ani_send')[:max_articles]
    
    for article in articles:
        title_tag = article.select_one('a.news_tit')
        desc_tag = article.select_one('div.news_dsc')
        
        title = title_tag['title'] if title_tag else ''
        link = title_tag['href'] if title_tag else ''
        description = desc_tag.text.strip() if desc_tag else ''
        summary = simple_summarize(description)
        
        results.append({
            'title': title,
            'link': link,
            'summary': description
        })
    
    return results

def simple_summarize(text, max_len=100):
    if not text:
        return ""
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit(' ', 1)[0] + "..."