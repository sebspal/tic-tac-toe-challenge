from flask_sqlalchemy import SQLAlchemy
from service.entities.match import Match
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class MatchModel(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(9), default=' ' * 9, nullable=False)
    turn = db.Column(db.String(1), default='X', nullable=False)
    state = db.Column(db.String(20), default='ongoing', nullable=False)


class MatchRepository:
    def next_id(self):
        try:
            return db.session.query(db.func.max(MatchModel.id)).scalar() or 0 + 1
        except SQLAlchemyError:
            db.session.rollback()
            return 1

    def save(self, match):
        try:
            match_model = MatchModel.query.get(match.match_id) or MatchModel(id=match.match_id)
            match_model.board = ''.join(match.board)
            match_model.turn = match.turn
            match_model.state = match.state
            db.session.add(match_model)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    def find_by_id(self, match_id):
        try:
            match_model = MatchModel.query.get(match_id)
            if match_model:
                return Match(
                    match_id=match_model.id,
                    board=list(match_model.board),
                    turn=match_model.turn,
                    state=match_model.state
                )
            return None
        except SQLAlchemyError:
            db.session.rollback()
            raise
