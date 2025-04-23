from flask import request, jsonify
from werkzeug.exceptions import BadRequest


class GameController:
    def __init__(self, game_service):
        self.game_service = game_service

    def create_match(self):
        try:
            match = self.game_service.create_match()
            return jsonify({"matchId": match.match_id}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def make_move(self):
        try:
            data = request.json
            if not data or 'matchId' not in data or 'playerId' not in data or 'square' not in data:
                raise BadRequest("Invalid request payload")

            match = self.game_service.make_move(
                data['matchId'],
                data['playerId'],
                data['square']['x'],
                data['square']['y']
            )
            return jsonify({
                "status": "Move accepted",
                "board": match.board,
                "turn": match.turn,
                "state": match.state
            }), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_status(self):
        try:
            match_id = request.args.get('matchId')
            if not match_id:
                raise BadRequest("matchId parameter is required")

            match = self.game_service.get_status(match_id)
            if not match:
                return jsonify({"error": "Match not found"}), 404

            return jsonify({
                "board": match.board,
                "turn": match.turn,
                "state": match.state
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500