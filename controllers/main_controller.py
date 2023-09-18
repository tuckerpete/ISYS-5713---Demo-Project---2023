from models import team_model
from models import game_model
from views import printer_view

def print_teams_ranked_by_ppg():

    # read in teams data
    teams = team_model.read_in_teams_data()

    # read in games data & add games to each team
    teams = game_model.read_in_games_data(teams)

    # rank teams from most to least ppg
    teams_sorted_by_ppg = team_model.rank_teams_by_ppg(teams)

    # output a pretty table
    printer_view.print_ppg_ranking_table(teams_sorted_by_ppg)