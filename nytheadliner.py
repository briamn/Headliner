import bs4, requests

url = 'http://nytimes.com'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
headline = [i for i in soup.select('h2.story-heading a')[0:8]]
headlines = []
for i in headline:
    headlines.append(i.getText().strip("\n "))
for i in headlines:
    print(i)
