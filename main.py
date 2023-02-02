
from send_email import send_email
import requests

topic = "entertainment"

api_key = "abdc73e693b94dae98b16b7845f97039"
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'sortBy=publishedAt&'
       'apiKey=abdc73e693b94dae98b16b7845f97039&'
       'language=en')

request = requests.get(url)

# Get a Dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + \
               "\n" + body + article["title"] + "\n" + \
               article["description"] + \
               "\n" + article["url"] + 2 * "\n"

# message = [article["title"] for article in content["articles"]]
# print(message)
#
body = body.encode("utf-8")
send_email(body)
