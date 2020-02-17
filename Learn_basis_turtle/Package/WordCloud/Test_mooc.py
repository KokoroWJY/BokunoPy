import wordcloud
import random

red = random.randint(0, 255)
green = random.randint(0,255)
blue = random.randint(0, 255)
txt = "life is short, you need python"
w = wordcloud.WordCloud()
w.generate(txt)
w.to_file("name.png")
