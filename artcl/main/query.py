from newspaper import Article
from nltk.stem import PorterStemmer
from artcl.utils.stopwords import StopWords

# Given keywords and query parameters, queries database to find most relevant articles
class Query:

	ps = PorterStemmer()

	def query(keywords, limit):

		return "success"