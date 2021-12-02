import pytest
import hashlib

from models.poll import Poll
from models.player import User


class TestGame:

    def test_game_raises_exception_if_only_one_player(self):
        with pytest.raises(Exception) as MissingPlayerException:
            game = Game([Player('Jonathan')])
        assert str(MissingPlayerException.value) == "Games must include 2 or more players."

    def test_game_sets_first_player_as_current(self):
        player1, player2 = Player('Jack'), Player('Jill')
        game = Game([player1, player2])
        assert game.current_player() == player1

    def test_game_code_generation(self):
        game = Game([Player('Jonathan'), Player('Sebastian')])
        assert len(game.code)
        assert len(game.code) == 6

    def test_next_player_works(self):
        player1, player2, player3 = Player('Jack'), Player('Jill'), Player('Jim')
        game = Game([player1, player2, player3])

        assert game.current_player() == player1
        game.next_player()
        assert game.current_player() == player2
        game.next_player()
        assert game.current_player() == player3
        game.next_player()
        assert game.current_player() == player1

    def test_next_player_works(self):
        player1, player2, player3 = Player('Jack'), Player('Jill'), Player('Jim')
        game = Game([player1, player2, player3])

        assert game.current_player() == player1
        assert game.round == 1

        game.next_player()
        game.next_player()
        game.next_player()
        assert game.round == 2

        game.next_player()
        game.next_player()
        game.next_player()
        assert game.round == 3

    def test_that_round_one_is_first(self):
        game = Game([Player('Jonathan'), Player('Sebastian')])
        assert game.round == 1