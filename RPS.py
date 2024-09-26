def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    prochaine_coup = 'R'
    if ((len(opponent_history) % 5 == 0) or (len(opponent_history) % 5 == 1)):
        if(opponent_history[-1] == 'P'):
            if(opponent_history[-2] == 'R'):
                
                prochaine_coup = 'S'
            else:
                prochaine_coup = 'S'
        else:
            prochaine_coup = 'P'
    elif ((len(opponent_history) % 5 == 2) or (len(opponent_history) % 5 == 3)):
        if(opponent_history[-1] == 'S'):
            if(opponent_history[-2] == 'R'):   
                    prochaine_coup = 'S'
            else:
                prochaine_coup ='R'
        else :
            prochaine_coup = 'S'
    elif(len(opponent_history) % 5 == 4):
        if(opponent_history[-1] == 'R'):
            if(opponent_history[-2] == 'R'):
                prochaine_coup = 'R'
            else:
                prochaine_coup = 'P'
        else:
            prochaine_coup = 'R'
    return prochaine_coup
