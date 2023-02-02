import smtplib
from send_email import send_email
import requests
import os
import ssl

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
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

# message = [article["title"] for article in content["articles"]]
# print(message)
#
body = body.encode("utf-8")
send_email(body)
