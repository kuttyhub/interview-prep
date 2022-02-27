def tournamentWinner(competitions, results):
    dic={}
    finalWinner =''
    finalScore =0
    for i in range(len(results)):
        matchTeam=competitions[i]
        winnerTeam= matchTeam[0] if results[i] == 1 else matchTeam[1]
            
        dic[winnerTeam]=dic.get(winnerTeam,0)+3
        if finalScore <dic[winnerTeam]:
            finalScore=dic[winnerTeam]
            finalWinner=winnerTeam

    return finalWinner

competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results=[0, 0, 1]

print(tournamentWinner(competitions,results))