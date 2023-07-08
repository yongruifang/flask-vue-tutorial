from flask import Flask, jsonify,request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origin':"*"}})

# hello world route
@app.route('/',methods=['GET'])
def greetings():
	return "Hello World!" 

# shark route
@app.route('/shark', methods=['GET'])
def shark():
	return "shark🦈"

GAMES = [
  {
    'id': uuid.uuid4().hex,
    'title': 'War',
    'genre': 'Tom',
    'played': 'false',
  },
  {
    'id': uuid.uuid4().hex,
    'title': '4399',
    'genre': 'Tom',
    'played': 'false',
  },
  {
    'id': uuid.uuid4().hex,
    'title': '7k7k',
    'genre': 'Tom',
    'played': 'true',
  },
  {
    'id': uuid.uuid4().hex,
    'title': 'saier',
    'genre': 'Tom',
    'played': 'false',
  },
  {
    'id': uuid.uuid4().hex,
    'title': 'luoke',
    'genre': 'Tom',
    'played': 'false',
  },
]

@app.route('/games', methods=['GET', 'POST'])
def allGames():
	response_object = {'status': 'success'}
	if request.method == 'POST':
		post_data = request.get_json()
		GAMES.append({
      			'id': uuid.uuid4().hex,
			'title': post_data.get('title'),
			'genre': post_data.get('genre'),
			'played': post_data.get('played')
		})
		response_object['message'] = 'Game Added!'
	else:
		response_object['games'] = GAMES
	return jsonify(response_object)

@app.route('/games/<game_id>', methods=['PUT','DELETE'])
def single_game(game_id):
  response_object = {'status': 'success'}
  if request.method == 'PUT':
    post_data = request.get_json()
    remove_game(game_id)
    GAMES.append({
      'id': uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played')
	})
    response_object['message'] = 'Game updated!'
  if request.method == "DELETE":
    remove_game(game_id)
    response_object['message'] = 'Game removed!'
  return jsonify(response_object)

def remove_game(game_id):
  for game in GAMES:
    if game['id'] == game_id:
      GAMES.remove(game)
      return True
  return False


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
