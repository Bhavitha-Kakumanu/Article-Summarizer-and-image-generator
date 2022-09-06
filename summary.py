$ python -m venv env
$ source env/bin/activate
$ pip install sumy wand newspaper3k requests numpy
import nltk
nltk.download('punkt')

from newspaper import Article

url = "https://arstechnica.com/science/2018/06/first-space-then-auto-now-elon-musk-quietly-tinkers-with-education/"
article = Article(url)
article.download()
article.parse()

print(article.images)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer

LANGUAGE = "english"
SENTENCES_COUNT = 10

parser = PlaintextParser.from_string(article.text, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)
summarizer = Summarizer(stemmer)

for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)

