import wordcloud
import os

filenames = list(os.walk("./exports/text"))[0][2]

with open("italian_stopwords.txt") as file:
    stopwords = set(file.read().split("\n"))

for filename in filenames:
    with open(f"./exports/text/{filename}", encoding="utf8") as f:
        data = f.read()
    try:
        newcloud = wordcloud.WordCloud(max_words=2000, width=1920, height=1080, stopwords=stopwords).generate(data)
        image = newcloud.to_image()
    except Exception as e:
        continue
    image.save(f"./exports/wordclouds/{filename.replace('.txt', '.png')}")
    print(f"./exports/wordclouds/{filename.replace('.txt', '.png')}")
