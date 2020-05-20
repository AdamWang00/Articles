from flask import jsonify, request, Blueprint
from artcl.main.index import Index

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

	return "todo"
	return jsonify()


@main.route('/api/index', methods=['GET'])
def api_index():
	if 'url' in request.args:
		url = str(request.args['url'])
	else:
		return "error: no url provided"

	return Index.index(url)
