#importing wikipedia articles of the Boston Bruins seasons (11' and 23')

from mediawiki import MediaWiki

wikipedia = MediaWiki()
bruins11 = wikipedia.page("2010–11 Boston Bruins season")
print(bruins11.title)
print(bruins11.content)

wikipedia = MediaWiki()
bruins11 = wikipedia.page("2022-23 Boston Bruins season")
print(bruins11.title)
print(bruins11.content)


# if __name__ == "__main__":
#     main()