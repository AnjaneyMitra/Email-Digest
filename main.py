import requests
from email_send import send_mail

key = "c2bed2dfb68d4740a19e81dc0bbf8954"
topic = tesla
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2024-02-11&" \
      "sortBy=publishedAt" \
      "&apiKey=c2bed2dfb68d4740a19e81dc0bbf8954&" \
      "language=en"

request = requests.get(url)
content = request.json()

body = f"" \
       "Subject: Today's News \n"
for article in content["articles"][:20]:
    body = body + str(article["title"]) + "\n" + str(article["description"])+ "\n" + str(article["url"]) + 2*"\n"

body = body.encode(("utf-8"))

send_mail(body)
