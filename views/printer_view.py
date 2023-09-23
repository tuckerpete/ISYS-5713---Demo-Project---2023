
def print_ppg_ranking_table(teams_sorted_by_ppg):
    # output a pretty table
    print("Rank\t| PPG\t| Team name")
    print("-----------------------------------")
    i = 0
    last_ppg = 9999999
    for school, ppg in teams_sorted_by_ppg:
        if ppg == 0:
            break
        if last_ppg != ppg:
            i = i + 1
        
        print(str(i) + "\t| " + str(round(ppg,2)) + "\t| " + school)

        last_ppg = ppg
