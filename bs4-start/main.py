from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/?p=2")

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
# first_article = soup.find(class_="titleline")
# anchor_text = first_article.a.getText()
# anchor_link = first_article.a.get("href")
# anchor_upvote = soup.find(class_="score").getText()
# print(anchor_upvote)
anchor_list = soup.select(".titleline > a")
score_list = soup.select(".subline > .score")

texts = [anchor.getText() for anchor in anchor_list]
links = [anchor.get("href") for anchor in anchor_list]
scores = [int(score.getText().split(" ")[0]) for score in score_list]

# print(text)
# print(link)
# print(score)
#
# print(len(anchor_list))
# print(len(score_list))

# hiscore_index = 0
# hiscore = scores[0]
# for i in range(1, len(scores)):
#     if scores[i] > hiscore:
#         hiscore = scores[i]
#         hiscore_index = scores.index()

highest_score = max(scores)
hiscore_index = scores.index(highest_score)

print(texts[hiscore_index])
print(links[hiscore_index])
print(highest_score)




# for score in score_list:
#     print(score.getText())
# for anchor in anchor_list:
#     print(anchor.getText())
#     print(anchor.get("href"))


