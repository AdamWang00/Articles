from newspaper import Article
from nltk.stem import PorterStemmer

class Index:

	ps = PorterStemmer()

	def index(url):
		article = Article(url)

		article.download()
		article.parse()

		print(article.text)
		return "success"