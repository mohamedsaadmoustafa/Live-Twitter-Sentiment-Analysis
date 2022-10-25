from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://www.englishclub.com/esl-chat/abbreviations.htm"  # change to whatever your url is

page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")
len(soup.find_all('table'))

chatwords = {}
soup.find_all('table')[1]
for table in soup.find_all('table'):
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        chatwords[tds[0].text.upper()] = tds[1].text

chatwords_df = pd.DataFrame(
    chatwords.items(),
    columns=['abbreviation', 'meaning'],
    index=np.arange(len(chatwords))
)
# save chatwords_df
chatwords_df.to_csv("./data/chatwords.csv", index=False)
print('Done!')