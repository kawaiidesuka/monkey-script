from random import shuffle
from random import randint
randnum = randint(0,29)
wordlib = ["tomato", "brick", "cheese", "banana", "eagle", "oil", "america", "guns", "bullets", "potato", "jews", "aphrodisiac", "bullseye", "heretic", "xenomorph", "cuddle", "bubble", "insomnia", "entropy", "dinosaur", "terminal", "python", "oasis", "snow", "animu", "dank", "weeaboo", "imageboard", "nano", "shakespeare", "kawaii", "neko", "aubergine", "eggplant", "oppression", "monkey", "shoe", "politics", "tumblr", "imageboard"]
shuffle(wordlib)
for wordlib[randnum] in wordlib:
	print wordlib[randnum]

