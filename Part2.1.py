#### Part 2: analyizing the text of the Boston Bruins seasons (11' and 23')
from mediawiki import MediaWiki

wikipedia = MediaWiki()
bruins11 = wikipedia.page("2010–11 Boston Bruins season")
# print(bruins11.title)
# print(bruins11.content)

wikipedia = MediaWiki()
bruins23 = wikipedia.page("2022-23 Boston Bruins season")
# print(bruins23.title)
# print(bruins23.content)

#### 2.1.) removing Stopping Words

# Removing Stopping Words for the 2010-11 season article

#this is the list of stop words that we will use to filter out common words
stop_words = ["the", "is", "in", "on", "at", "a", "an", "of", "and", "==", "to", "for", "with", "by", "this", "that", "as", "it", "was", "were", "be", "are", "not", "but", "or", "from", "which", "about", "all", "any", "there", "if", "more", "than", "so", "its", "they"]

# this is the text of the 2010-11 season article
bb11_text = (bruins11.content) 

# this splits the text into words
words11 = bb11_text.split()

# this filters out the stop words
filtered_words = [word for word in words11 if word.lower() not in stop_words] 
# print(filtered_words)

# Removing Stopping Words for the 2022-23 season article 

#this is the list of stop words that we will use to filter out common words 
stop_words = ["the", "is", "in", "on", "at", "a", "an", "of", "and", "==", "===" "to", "for", "with", "by", "this", "that", "as", "it", "was", "were", "be", "are", "not", "but", "or", "from", "which", "about", "all", "any", "there", "if", "more", "than", "so", "its", "they"]

# this is the text of the 2022-23 season article
bb23_text = (bruins23.content)

# this splits the text into words
words23 = bb23_text.split()

# this filters out the stop words
filtered_words = [word for word in words23 if word.lower() not in stop_words]

print(filtered_words)

