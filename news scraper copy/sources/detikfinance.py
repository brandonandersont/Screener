import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class DetikFinance:
    def __init__(self):
        self.base_url = 'https://finance.detik.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'}
        self.response = requests.get(self.base_url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
    
    def keyword_detikfinance(self, keywords):
        results, seen = [], set()
        for keyword in keywords:
            search_url = f"https://www.detik.com/search/searchall?query={keyword}&siteid=29&source_kanal=true"
            print(f"Fetching for {keyword}...")

            try:
                self.response = requests.get(search_url, headers=self.headers)
                if self.response.status_code!=200:
                    print(f"Failed to fetch data for {keyword} - Status: {self.response.status_code}")
                    continue

                self.soup = BeautifulSoup(self.response.text, "html.parser")
            except requests.RequestException as e:
                print(f"Network error for {keyword}: {e}")
                continue

            articles = self.soup.select("article")
            if not articles:
                print(f"No articles found for {keyword}")
                continue

            print(f"Found {len(articles)} articles, processing...")

            for article in articles:
                url_element = article.find(attrs=({"dtr-ttl": True})) or article.find('a', href=True)
                if not url_element or not url_element.get("href"):
                    continue

                date = article.find('div', class_='media__date')
                date_text = date.get_text(strip=True) if date else "No date available"
                if not date:
                    continue

                title = (url_element.get("dtr-ttl") or (article.select_one('h1, h2, h3').get_text(strip=True) if article.select_one('h1, h2, h3') else ''))
                if not title:
                    continue

                link = urljoin(self.base_url, url_element['href'])
                if link in seen:
                    continue
                    
                seen.add(link)
                results.append({
                    "keyword": keyword,
                    "title": title,
                    "link": link,
                    "date": date_text,
                })

        return results

if __name__ == "__main__":
        detikfinance = DetikFinance()
        keyword = input("Enter a keyword: ")
        results = detikfinance.keyword_detikfinance([keyword.capitalize()])
        for result in results:
            print(f"Keyword: {result['keyword']}")
            print(f"{result['date']} | Title: {result['title']}")
            print(f"Link: {result['link']}")
            print()