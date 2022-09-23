import multidict as multidict

import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def getFrequencyDictForText(count_dict):
    fullTermsDict = multidict.MultiDict()

    #import ipdb
    #ipdb.set_trace()
    for key in count_dict:
        fullTermsDict.add(key, count_dict[key])
    return fullTermsDict
def get_count_dict():
    f = open('count_dict.txt','r').readlines()
    #count_dict = dict([(k,v) for k,v in f])
    count_dict = {}
    for line in f:
        line = line.strip()
        li = line.split('\t')
        value = li[0]
        key = li[1]
        value = eval(value)
        value = value * 1000000000
        value = int(value)
        count_dict[key]=value

    return count_dict
def makeImage(text):
    #alice_mask = np.array(Image.open("alice_mask.png"))
    alice_mask = np.array(Image.open("8416.jpg_wh1200.jpg"))

    wc = WordCloud(font_path='AaShiSongTi-2.ttf',background_color="white", max_words=1000, mask=alice_mask)
    # generate word cloud
    #import ipdb
    #ipdb.set_trace()
    wc.generate_from_frequencies(text)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
if __name__ == '__main__':
    count_dict = get_count_dict()
    text = getFrequencyDictForText(count_dict)
    makeImage(text)
