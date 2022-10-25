from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = "https://www.emoticonr.com/emoticons"  # change to whatever your url is

page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

smileys = {}
for div in soup.find_all("div", {"class": "tableText"}):
    divs = div.find_all("div")
    smileys[divs[1].text] = divs[0].text

#
smileys_df = pd.DataFrame(
    smileys.items(),
    columns=['smiley', 'meaning'],
    index=np.arange(len(smileys))
)
# save smileys_df
smileys_df.to_csv("./data/smileys.csv", index=False)
print('Done!')