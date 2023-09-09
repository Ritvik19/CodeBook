# O(n) O(m)

def tournamentWinner(competitions, results):
    score_board = {}
    current_best_team = ""
    for teams, result in zip(competitions, results):
        winning_team = teams[1-result]
        score_board[winning_team] = score_board.get(winning_team, 0) + 1
        if score_board.get(current_best_team, 0) < score_board[winning_team]:
            current_best_team = winning_team
            
        
    return current_best_team
tournamentWinner(**{
  "competitions": [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ],
  "results": [0, 0, 1]
})