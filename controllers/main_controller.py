from models import team_model
from models import game_model
from models import base_model
from views import printer_view
from controllers import api_controller


def load_data_and_start_api():

    # create our database if it doesn't exist
    base_model.create_database()

    # read in teams data
    team_model.read_in_teams_data()

    # read in games data & add games to each team
    game_model.read_in_games_data()

    # start API server
    api_controller.run()
