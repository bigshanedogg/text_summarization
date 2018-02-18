# Text Summarization<br>
<br>

## text_rank.py
"text_rank.py" is the code to summarize the text, among which news articles. <br>
The summary is processed in the following order:

1. Determine the length of the summary statement according to the number of sentences given.
2. Divide the text into sentences, and break the sentence into morphemes to create a tfidf matrix.
3. The Page Rank algorithm is applied to the product of this tfidf matrix and transpose matrix to prioritize the importance of each sentence in the text.
4. Join the upper priority sentence corresponding to the length of the summary statement defined above.

<hr>
<br>

## How to use
#### 1) Import module and sample article data
<pre><code>import text_rank as tr<br>
news1 = ''
with open("../sample_data/news1.txt", mode="r") as fp :
    news1 = fp.read()
</code></pre>

#### 2) Creat text_rank object
<pre><code>summarizer = tr.text_rank(news1)
print("Sentences length before summarization :", summarizer.sentences_n)
print("Text :\n", summarizer.text)
</code></pre>

#### 3) Check the summarized text
<pre><code>summary = summarizer.get_summary()
print("\nSentences length after summarization :", summarizer.summary_n)
print("Summary :\n",summary)
</code></pre>
<br><br>
<hr>
This code has been fitted to Naver news article, which can be seperated with ".". Kkma.sentences() method of Konlpy package - Korean Natural Language PYthon is more appropriate to split other unstructured data such as SNS buzz into sentences because there is no rule to distinguish sentences like "." in general case. Kkma sometimes has the mistake of separating the main clause and subordinate clause, but I think it is the best one in this case. (I usually prefer mecab-ko for morpheme analysis, but mecab-ko pakcage does not support sentences function yet.)
