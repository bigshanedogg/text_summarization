# -*- coding: utf-8 -*-
import text_rank as tr

news1 = ''
with open("../sample_data/news1.txt", mode="r") as fp :
    news1 = fp.read()

summarizer = tr.text_rank(news1)
print("Sentences length before summarization :", summarizer.sentences_n)
print("Text :\n", summarizer.text)
summary = summarizer.get_summary()
print("\nSentences length after summarization :", summarizer.summary_n)
print("Summary :\n",summary)

