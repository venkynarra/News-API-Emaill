import requests
api_key = "b7adf25b371946b3b97a5b2321aada9e"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-06&sortBy=publishedAt&apiKey=b7adf25b371946b3b97a5b2321aada9e"
request = requests.get(url)
# get a dictionary with data
content = request.json()

# access the article title and description
print(content["articles"])
for article in content["articles"]:
    print(article["title"])
    print(article["description"])