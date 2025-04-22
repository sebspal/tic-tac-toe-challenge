from flask import request, jsonify
from service.usecases.game_service import GameService


class GameController:
    def __init__(self, game_service):
        self.game_service = game_service

    def create_match(self):
        match = self.game_service.create_match()
        return jsonify({"matchId": match.match_id}), 200

    def make_move(self):
        data = request.json
        match = self.game_service.make_move(data['matchId'], data['playerId'], data['square']['x'], data['square']['y'])
        return jsonify({"status": "Move accepted"}), 200

    def get_status(self):
        match_id = request.args.get('matchId')
        match = self.game_service.get_status(match_id)
        return jsonify({
            "board": match.board,
            "turn": match.turn,
            "state": match.state
        }), 200
