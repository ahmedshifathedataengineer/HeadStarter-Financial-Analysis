from newspaper import Article

def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "author": article.authors,
            "publish_date": article.publish_date,
            "text": article.text
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None
