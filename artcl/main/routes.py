from flask import jsonify, request, Blueprint
from artcl.main.index import Index
from artcl.main.query import Query

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
	return "homepage"


@main.route('/api/query', methods=['GET'])
def api_query():
	if 'keywords' in request.args:
		keywords = request.args['keywords']
	else:
		return "error: no keywords provided"

	if 'limit' in request.args:
		limit = request.args['limit']
	else:
		limit = 10

	res = Query.query(keywords, limit)

	return "todo"
	return jsonify()


@main.route('/api/index', methods=['GET'])
def api_index():
	if 'url' in request.args:
		url = str(request.args['url'])
	else:
		return "error: no url provided"

	x = Index.index(url)
	return "todo" + x
	return jsonify()
