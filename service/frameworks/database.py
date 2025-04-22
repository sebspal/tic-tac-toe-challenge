from flask_sqlalchemy import SQLAlchemy
from service.entities.match import Match

db = SQLAlchemy()


class MatchModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(9), default=' ' * 9)
    turn = db.Column(db.String(1), default='X')
    state = db.Column(db.String(10), default='ongoing')


class MatchRepository:
    def next_id(self):
        return MatchModel.query.count() + 1

    def save(self, match):
        match_model = MatchModel.query.get(match.match_id) or MatchModel(id=match.match_id)
        match_model.board = ''.join(match.board)
        match_model.turn = match.turn
        match_model.state = match.state
        db.session.add(match_model)
        db.session.commit()

    def find_by_id(self, match_id):
        match_model = MatchModel.query.get(match_id)
        if match_model:
            return Match(match_id=match_model.id, board=list(match_model.board), turn=match_model.turn,
                         state=match_model.state)
        return None
