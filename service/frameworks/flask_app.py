from flask import Flask
from service.frameworks.database import db
from service.controllers.match_controller import GameController
from service.usecases.game_service import GameService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tictactoe.db'
db.init_app(app)

game_service = GameService(match_repository=db)
game_controller = GameController(game_service)

@app.route('/create', methods=['POST'])
def create_match():
    return game_controller.create_match()

@app.route('/move', methods=['POST'])
def make_move():
    return game_controller.make_move()

@app.route('/status', methods=['GET'])
def get_status():
    return game_controller.get_status()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
