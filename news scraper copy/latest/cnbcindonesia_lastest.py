import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class CNBCIndonesia_latest:
    def __init__(self):
        self.base_url = 'https://www.cnbcindonesia.com/market/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'}
        self.response = requests.get(self.base_url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
    
    def latest_cnbcindonesia(self):
        results, seen = [], set()

        for art in self.soup.select('article'):
            a = art.find(attrs={"dtr-ttl": True}) or art.find('a', href=True)
            if not a or not a.get("href"):
                continue

            date = art.select_one('.flex.flex-wrap .text-xs.text-gray, .flex.flex-wrap .text-xs.text-gray-light5')
            date_text = date.get_text(strip=True) if date else "No date available"

            link = urljoin(self.base_url, a['href'])
            if link in seen:
                continue

            title = (a.get("dtr-ttl") or (art.select_one('h1, h2, h3').get_text(strip=True) if art.select_one('h1, h2, h3') else ''))
            if not title:
                continue

            seen.add(link)
            results.append({
                "keyword": "Latest",
                "title": title,
                "link": link,
                "date": date_text
            })
            
        return results

if __name__ == "__main__":
    cnbc_latest = CNBCIndonesia_latest()
    articles = cnbc_latest.latest_cnbcindonesia()
    count = 0
    for result in articles:
        print(f"Keyword: {result['keyword']}")
        print(f"{result['date']} | {result['title']}")
        print(result['link'])
        print()
        count += 1
    
    print(f"Total articles fetched: {len(articles)}")
   


