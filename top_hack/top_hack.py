import time
import requests
from bs4 import BeautifulSoup

class TopHack:

    def __init__(self, amount=10, min_score=100):
        self.url = "https://news.ycombinator.com"
        self.session = requests.Session()
        self.amount = amount
        self.min_score = min_score
        self.results = []
        self.sleep = 3

    def _get_html(self, page=1):
        response = self.session.get(self.url, params={'p': page})
        return response.text

    def _get_urls(self, text):
        soup = BeautifulSoup(text, 'html.parser')

        found = []

        for node in soup.select('.athing .title .titlelink'):

            found.append({
                "title": node.string,
                "url": node['href']
            })

        for idx, score in enumerate(soup.select('.score')):

            num, _ = score.string.split(" ")
            found[idx]['score'] = int(num)

        self.results += [*found]

    def _filter(self):
        filtered = []

        for result in self.results:

            if result['score'] >= self.min_score:
                filtered.append(result)

        self.results = filtered

    def _sort(self):

        self.results = sorted(
            self.results,
            key=lambda result: result['score'])

    def run(self):

        page = 1

        while len(self.results) < self.amount:

            html = self._get_html(page=page)
            self._get_urls(html)
            time.sleep(self.sleep)
        self._filter()
        self._sort()
        return self.results

