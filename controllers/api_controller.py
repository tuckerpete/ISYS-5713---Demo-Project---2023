from models import team_model
from views import api_view

from flask import Flask, jsonify, request

app = Flask(__name__)

def run():
    # Start the API server
    app.run(debug=True)

@app.route("/hello", methods=['GET'])
def hello_world():
    return "<h1>Hello, World!</h1>"

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
    new_team = team_model.create_team(team_data)
    return jsonify(new_team.as_dict()), 200


@app.route("/teams/<int:team_id>", methods=['DELETE'])
def delete_team(team_id):
    it_worked = team_model.delete_team(team_id)
    if it_worked == True:
        return "Success", 200
    else:
        return f"Error: Team with ID {team_id} does not exist", 404

@app.route("/teams/<int:team_id>", methods=['PUT'])
def update_team(team_id):
    team_data = request.get_json()
    updated_team = team_model.update_team(team_id, team_data)
    if updated_team is not None:
        return jsonify(updated_team.as_dict()), 200
    else:
        return f"Error: Team with ID {team_id} does not exist", 404

@app.route("/teams", methods=['GET'])
def get_teams():
    conference = request.args.get('conference', default=None, type=str)
    teams = team_model.get_teams(conference=conference)
    if teams is not None:
        return jsonify([team.as_dict() for team in teams]), 200
    else:
        return f"Error: No teams found", 404

