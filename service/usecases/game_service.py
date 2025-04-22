from service.entities.match import Match


class GameService:
    def __init__(self, match_repository):
        self.match_repository = match_repository

    def create_match(self):
        match = Match(match_id=self.match_repository.next_id())
        self.match_repository.save(match)
        return match

    def make_move(self, match_id, player, x, y):
        match = self.match_repository.find_by_id(match_id)
        match.make_move(player, x, y)
        self.match_repository.save(match)
        return match

    def get_status(self, match_id):
        return self.match_repository.find_by_id(match_id)
