from flask import Flask
from flask_cors import CORS
from service.frameworks.database import db
from service.controllers.match_controller import GameController
from service.usecases.game_service import GameService
from service.frameworks.database import MatchRepository
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    match_repository = MatchRepository()
    game_service = GameService(match_repository)
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

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
