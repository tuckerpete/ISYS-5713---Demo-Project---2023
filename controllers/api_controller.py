from models import team_model
from views import api_view

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello_world():
    return "<h1><b>Hello</b>, World!</h1>"


@app.route("/ppg", methods=['GET'])
def get_ppg():
    # optional param for limit
    limit = request.args.get('limit', default=100, type=int)

    # rank teams from most to least ppg
    teams_sorted_by_ppg = team_model.rank_teams_by_ppg()

    # output a pretty table
    ranked_teams = api_view.print_ppg_ranking_table(teams_sorted_by_ppg)[:limit]

    return jsonify(ranked_teams), 200


@app.route("/teams/<int:team_id>", methods=['GET'])
def get_team(team_id):
    team = team_model.get_team(team_id)
    if team is not None:
        return jsonify(team.as_dict()), 200
    else:
        return f"Error: Team id {team_id} does not exist in the databse", 404

@app.route("/teams", methods=['POST'])
def create_team():
    team_data = request.get_json()
    new_team_id = team_model.create_team(team_data)
    return jsonify(team_model.get_team(new_team_id).as_dict()), 200


@app.route("/teams/<int:team_id>", methods=['DELETE'])
def delete_team(team_id):
    it_worked = team_model.delete_team(team_id)
    if it_worked == True:
        return "Success", 200
    else:
        return f"Error: Team with ID {team_id} does not exist"


def run():
    # Start the API server
    app.run(debug=True)