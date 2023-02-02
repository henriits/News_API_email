import requests


api_key = "abdc73e693b94dae98b16b7845f97039"
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-02-02&'
       'sortBy=popularity&'
       'apiKey=abdc73e693b94dae98b16b7845f97039')

request = requests.get(url)

# Get a Dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])