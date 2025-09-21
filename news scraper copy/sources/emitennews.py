import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class EmitenNews:
    def __init__(self):
        self.base_url = 'https://emitennews.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'}
        self.response = requests.get(self.base_url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        
    def keyword_emitennews(self, keywords):
        results, seen = [], set()
        for keyword in keywords:
            search_url = f"{self.base_url}search/{keyword}"
            print(f"Fetching for {keyword}...")

            try:
                self.response = requests.get(search_url, headers=self.headers)
                if self.response.status_code != 200:
                    print(f"Failed to fetch data for {keyword} - Status: {self.response.status_code}")
                    continue

                self.soup = BeautifulSoup(self.response.text, "html.parser")
            except requests.RequestException as e:
                print(f"Network error for {keyword}: {e}")
                continue

            articles = self.soup.select("a.news-card-2.search-result-item")
            if not articles:
                print(f"No articles found for {keyword}")
                continue

            print(f"Found {len(articles)} articles, processing...")

            for article in articles:
                # Get the link
                link = article.get('href')
                if not link:
                    continue
                
                # Make sure it's a full URL
                if not link.startswith('http'):
                    link = urljoin(self.base_url, link)
                
                if link in seen:
                    continue

                # Get the title from p.fs-16
                title_elem = article.select_one('p.fs-16')
                if not title_elem:
                    continue
                title = title_elem.get_text(strip=True)
                if not title:
                    continue

                # Get the date from span.small inside .label
                date_elem = article.select_one('.label span.small')
                date_text = date_elem.get_text(strip=True) if date_elem else "No date available"

                seen.add(link)
                results.append({
                    "keyword": keyword,
                    "title": title,
                    "link": link,
                    "date": date_text,
                })

        return results
    
if __name__ == "__main__":
        emitennews = EmitenNews()
        keyword = input("Enter a keyword: ")
        results = emitennews.keyword_emitennews([keyword.capitalize()])
        for result in results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | Title: {result['title']}")
            print(f"Link: {result['link']}")
            print()