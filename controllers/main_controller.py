from models import db_model
from views import printer_view

def print_teams_ranked_by_ppg():

    # create the database if it doesn't exist already
    db_model.create_database()

    # read in teams data
    db_model.read_in_teams_data()

    # read in games data & add games to each team
    db_model.read_in_games_data()

    # rank teams from most to least ppg
    teams_sorted_by_ppg = db_model.rank_teams_by_ppg()

    # output a pretty table
    printer_view.print_ppg_ranking_table(teams_sorted_by_ppg)