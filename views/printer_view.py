
def print_ppg_ranking_table(teams_sorted_by_ppg):
    # output a pretty table
    print("Rank\t| PPG\t| Team name")
    print("-----------------------------------")
    i = 0
    last_ppg = 9999999
    for team_object in teams_sorted_by_ppg:
        ppg = team_object.ppg
        if ppg == 0:
            break
        if last_ppg != ppg:
            i = i + 1
        
        print(str(i) + "\t| " + str(ppg) + "\t| " + team_object.school)

        last_ppg = ppg