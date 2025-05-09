from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = []
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', class_='result__a', limit=10)
        for link in links:
            title = link.get_text()
            href = link['href']
            results.append({'title': title, 'link': href})
    else:
        results.append({'title': 'Error fetching results', 'link': '#'})

    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
