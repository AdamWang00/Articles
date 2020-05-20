from newspaper import Article
from nltk.stem import PorterStemmer
from artcl.utils.stopwords import StopWords

# Given article url, indexes article by extracting main text and storing information in databases
class Index:

	ps = PorterStemmer()

	def index(self, url):
		article = Article(url)

		article.download()
		article.parse()

		print(article.text)
		return "success"