from typing import List, Callable

from replay_analysis.generated.api import team_pb2
from ....json_parser.game import Game


class ApiTeam:
    @staticmethod
    def create_teams_from_game(game: Game, id_creator: Callable) -> List[team_pb2.Team]:
        teams = []
        for team in game.teams:
            proto_team = team_pb2.Team()
            if team.name is not None:
                proto_team.name = str(team.name)
            for player in team.players:
                id_creator(proto_team.player_ids.add(), player.name)
            proto_team.is_orange = team.is_orange
            proto_team.score = team.score
        return teams