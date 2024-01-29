import json
import requests
from bs4 import BeautifulSoup

result = []

page = requests.get("https://time.com", verify=False, timeout=10)
soup = BeautifulSoup(page.content, "html.parser")
recents = soup.find_all("li", class_="latest-stories__item")
for item in recents:
    print(item)
    link = "https://time.com" + (item.find_all("a")[0]["href"])
    title = item.find_all("h3")[0].text.strip()
    time = item.find_all("time")[0].text.strip()
    print(link)
    print(title)

    result.append({"title": title, "link": link, "time": time})

print(json.dumps(result, indent=2))
