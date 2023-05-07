#* regex practice

import re
import random

#*##################

# beans = "Fuck, I have a headache"
# x = re.findall("head",beans)
# print(x)
#$$$ uses re's "findall" function to look for "head" in beans.

#*##################

# banana = "The best fuckin fruit"
# x = re.search("fuck", banana)
# # print('Match starts at index space: ',x.start())
# #or
# print('Search Results: ', x)

#$$$ searches for 'fuck' in banana and you can output the
#$$$ starting index location or the start and end index together

#*##################

# da_colors = random.choice(['purple','pancake','conspiracy theories'])
#
# benshapiros_leftnut = ("My favorite color is: {}".format(da_colors))
# x = re.split(':', benshapiros_leftnut)
# print(x)

#$$$ This will use the split function to split "benshapiros_leftnut" at the ":"
#$$$ and randomly choose a random item from "da_colors"

#*##################

# pickle_wrecker = "It's 3AM and I'm hungry as shit and tired as fuck"
# x = re.sub("i|u","~", pickle_wrecker)
# print(x)

#$$$ This uses 're.sub' to substitute
#$$$ any lowercase i's and u's in pickle_wrecker with a "~"

#*##################

here_we_go = "Some say the wild fuckeroo is a mythical beast of epic proportions. It can be found in the wild " \
             "badlands of fuck-this-shit-istan and feeds on give-a-damns and the number 8."




