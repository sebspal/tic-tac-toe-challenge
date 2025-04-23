import pytest
from service.usecases.game_service import GameService
from service.frameworks.database import db, MatchRepository

@pytest.fixture
def match_repository(app):
    with app.app_context():
        db.create_all()
        yield MatchRepository()
        db.drop_all()

@pytest.fixture
def game_service(match_repository):
    return GameService(match_repository)

def test_create_match(game_service):
    match = game_service.create_match()
    assert match.match_id == 1
    assert match.board == [' '] * 9
    assert match.turn == 'X'
    assert match.state == 'ongoing'

def test_make_move(game_service):
    match = game_service.create_match()
    updated_match = game_service.make_move(match.match_id, 'X', 1, 1)
    assert updated_match.board[0] == 'X'
    assert updated_match.turn == 'O'