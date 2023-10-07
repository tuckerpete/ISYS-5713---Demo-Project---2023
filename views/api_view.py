
def print_ppg_ranking_table(teams_sorted_by_ppg):

    ranked_teams = []

    i = 0
    last_ppg = 9999999
    for team_school, ppg in teams_sorted_by_ppg:
        if ppg == 0:
            break
        if last_ppg != ppg:
            i = i + 1
        
        # print(str(i) + "\t| " + str(round(ppg,2)) + "\t| " + team_school)
        ranked_teams.append({
            'rank': i,
            'ppg': round(ppg,2),
            'team':team_school
        })


        last_ppg = ppg

    return ranked_teams
