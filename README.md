# Text-Analysis-Project
# Intro: (Project overview) 1 paragraph 
Growing up in a hockey household, I have been raised to be a Boston Bruins fan. This team has been a large part of my life and sadly, my mental health (depending on how they do in the play-offs). I was lucky enough to watch them win a Stanley cup in 2011 which could be one of the best days of my life and I have watched them make history and set records as the best team in the league, only to lose in the first round of playoffs in 2023. Which is up there for one of worst days in my life. Using Wikipedia as my data source, I want to compare what each article has to say about each season. I will be using techniques such as characterizing by word frequencies, computing summary statistics, and removing stop words to test the data. I am hoping to find the most frequently used words in each article, the statistics of the top 5 words used to describe the bruins’ seasons and compare the text similarity between the articles. I hope to learn how to use real life API’s so that I can apply them to future projects whether it is qualitative or quantitative. 
# Implementations: 1 – 2 paragraphs 
For the implementation of text analysis on the 2011 and 2023 Bruins season articles, the primary focus was on preprocessing the text, removing stop words, and then computing summary statistics, such as the top 10 most frequent words. I began by extracting the raw text of both articles and preprocessing it to remove any unwanted spaces, punctuation, and irrelevant stop words (common words like "the", "and", etc., that don't contribute much to meaningful analysis). To remove stop words, I created a custom list, filtering them out from the tokenized text. The next step was tokenization, where the text was split into individual words, and all words were converted to lowercase to ensure consistency in frequency counts. I then applied the Counter class to compute the frequency of each word, and used to extract the top 10 words in both seasons' articles, which helped characterize the content of each article by highlighting the most frequently mentioned terms.
In terms of design decisions, I chose Matplotlib to create a histogram of word frequencies, as it allowed for clear data visualization and easy annotations of the frequency of each word. Through Generative AI, I learned how to integrate text cleaning, tokenization, and frequency counting seamlessly into my workflow. AI suggestions also guided me in adding the frequency labels directly to the bars in the histogram, ensuring a clear and informative presentation of the data. Additionally, using AI helped streamline the process of automating the analysis for two different articles, ensuring the system could handle both the 2011 and 2023 seasons with minimal adjustments, allowing for easy comparison.
# Results: (1 – 3 paragraphs  + figures and examples)
In analyzing the 2011 and 2023 Bruins season articles, I discovered some intriguing insights regarding the frequency of terms used across both seasons. For example, in the 2011 article, terms like "Stanley Cup," "playoffs," and "victory" were prominent, reflecting the team's historic win. On the other hand, the 2023 article highlighted terms such as "record-breaking," "goals," and "season," pointing to the team's extraordinary performance that year, with a focus on statistics and milestones. These differences in the most common words provide a clear contrast between a season defined by a championship victory and one focused on achieving individual records. 
I then created these graphs to show the top 10 most frequent words in both articles. From here I can see what were the most frequently used words in each article and how they compared to the rest. 
 
 
It can bee season that in 23’, the Bruins most winningest season, the word “win” was one of the more frequently used words in the article. 
# Reflection (1 -2 paragraphs) 
Overall, the project went well, particularly in automating the text analysis process for both the 2011 and 2023 Bruins season articles. The word frequency analysis and data visualization using histograms provided valuable insights into the themes of each season. My biggest challenge was ensuring the accuracy of the text cleaning and stop word removal process, as some common words may not be relevant in all contexts. To solve this, I carefully crafted a stop word list and relied on regular expressions to properly clean and tokenize the text. While the project was generally well-scoped, there could have been more in-depth analysis, such as exploring sentiment or context around the most frequent terms. A more robust testing plan would have included validating the stop word removal and word count algorithms with different types of text data to ensure the program's accuracy. Overall, the project was a success, but refining the text cleaning steps and expanding the scope to include additional text analysis techniques would improve it further.
My biggest take away from this project is the partnership and support that generative AI can offer. I some situations I found myself struggling to come up with the correct code that will allow me to show case my data or filter out stopping words to get better quality data 
My process of using generative Ai looked like this: 
Asking Generative AI for Help
-	how do I get rid up spaces and punctation? 
-	how can I create data visualization in python? instead of creating an excel sheet an manually entering data?
-	how to add numbers to my histogram 
what was the problem?
-	I was trying to create a histogram of the word frequencies in the text, but I was not sure how to do it.
-	I was also trying to figure out how to remove spaces and punctuation from the text before counting word frequencies. 
What was the question I asked Generative AI?
-	how do I add the corresponding frequencies in the histogram
-	how can I create a histogram to show the word and its frequencies? "
-	  


# Please Look at "images" to see the graphs and generative AI prompts and solutions I got. 


Please read the [instructions](instructions.md).
