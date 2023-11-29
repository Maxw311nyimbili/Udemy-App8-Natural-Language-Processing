import re
import nltk
#nltk.download()

from nltk.corpus import stopwords

with open("miracle_in_the_andes.txt", "r", encoding="UTF-8") as file:
    book = file.read()

pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

dict_1 = {}
for word in findings:
    if word in dict_1.keys():
        dict_1[word] = dict_1[word] + 1
    else:
        dict_1[word] = 1


d_list = [(value, key) for (key, value) in dict_1.items()]
sorted(d_list[:3], reverse=True)


english_stopwords = stopwords.words("english")


filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))
#print(sorted(filtered_words, reverse=True))

# Finding the mood of the text.
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# mood_dict = analyzer.polarity_scores(book)
# if mood_dict["pos"] > mood_dict["neg"]:
#     print("the mood is positve")
# elif mood_dict["pos"] > mood_dict["neg"]:
#     print("the mood is negative")



