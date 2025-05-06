import requests
from send_email import send_email

api_key = "b7adf25b371946b3b97a5b2321aada9e"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-06&sortBy=publishedAt&apiKey=b7adf25b371946b3b97a5b2321aada9e&language=en"
request = requests.get(url)
# get a dictionary with data
content = request.json()

# access the article title and description
body = "Subject: Today's News\n\n"
for article in content["articles"][0:20]:
    body = body + (article.get("title") or "")+ "\n" + (article.get("description") or "")+ "\n" + article["url"]+2 * "\n"

body = body.encode("utf-8")
send_email(message=body)