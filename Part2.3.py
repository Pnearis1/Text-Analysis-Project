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
stop_words = ["the", "is", "in", "on", "at", "a", "an", "of", "and", "==", "to", "for", "with", "by", "this", "that", "as", "it", "was", "were", "be", "are", "not", "but", "or", "from", "which", "about", "all", "any", "there", "if", "more", "than", "so", "its", "they", "=", "===", "their"]

# this is the text of the 2010-11 season article
bb11_text = (bruins11.content) 

# this splits the text into words
words11 = bb11_text.split()

# this filters out the stop words
filtered_words11 = [word for word in words11 if word.lower() not in stop_words] 
# print(filtered_words)

# Removing Stopping Words for the 2022-23 season article 

#this is the list of stop words that we will use to filter out common words 
stop_words = ["the", "is", "in", "on", "at", "a", "an", "of", "and", "==", "===", "to", "for", "with", "by", "this", "that", "as", "it", "was", "were", "be", "are", "not", "but", "or", "from", "which", "about", "all", "any", "there", "if", "more", "than", "so", "its", "they", "their", "also"]

# this is the text of the 2022-23 season article
bb23_text = (bruins23.content)

# this splits the text into words
words23 = bb23_text.split()

# this filters out the stop words
filtered_words23 = [word for word in words23 if word.lower() not in stop_words]

# print(filtered_words)

#### 3.) Computing Summary Statistics

from collections import Counter
import re

# Get the text of the 2010-11 season article
text11 = (bruins11.content)

# Tokenize the text by splitting by space and removing punctuation and Convert text to lowercase to make counting case-insensitive
words = re.findall(r'\b\w+\b', text11.lower())  

# Create a Counter to count word frequencies
word_freq = Counter(filtered_words11)

# Get the top 10 most common words
top_10_words11 = word_freq.most_common(10)

# Display the top 10 most common words
print("Top 10 most common words in 2011 atricle:")
for word, count in top_10_words11:
    print(f"{word}: {count}") 

# Get the text of the 2022-23 season article
text23 = (bruins23.content)

# Tokenize the text by splitting by space and removing punctuation
words = re.findall(r'\b\w+\b', text11.lower())  # Convert text to lowercase to make counting case-insensitive

# Create a Counter to count word frequencies
word_freq = Counter(filtered_words23)

# Get the top 10 most common words
top_10_words23 = word_freq.most_common(10)

# Display the top 10 most common words
print("Top 10 most common words in 2023 atricle:")
for word, count in top_10_words23:
    print(f"{word}: {count}") 


##### Create a bar plot (histogram) of word frequencies of 2011 season article
import matplotlib.pyplot as plt 

words, counts = zip(*top_10_words23) # Unzip the words and counts 

plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(words, counts, color='skyblue')

# Add labels and title
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in 2023 Article')

# Show the plot
plt.xticks(rotation=45)  # Rotate the x-axis labels for readability

plt.yticks(range(0, max(counts) + 1, 1))  # y-ticks from 0 to the maximum count, with a step size of 1

plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()

##### Create a bar plot (histogram) of word frequencies of 2011 season article
words, counts = zip(*top_10_words11)

# Create a bar plot (histogram) of word frequencies
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(words, counts, color='skyblue')

# Add labels and title
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in 2011 Article')

# Show the plot
plt.xticks(rotation=45)  # Rotate the x-axis labels for readability 

plt.yticks(range(0, max(counts) + 1, 1))  # y-ticks from 0 to the maximum count, with a step size of 1 

plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()