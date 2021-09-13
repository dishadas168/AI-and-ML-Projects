# export
def minimax(player, game, time_left, depth, my_turn=True, last_move=(-1, -1, 0)):
    """Implementation of the minimax algorithm.

    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you
            need from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer()).
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """
    # TODO: finish this function!

    if depth == 0:
        # player = game.get_inactive_player()
        print(depth, ' 2.1')
        if player.__class__.__name__ == 'RandomPlayer':
            bestVal = len(game.get_player_moves(player)) - len(game.get_opponent_moves(player))
            print(depth, ' 2.1RP')
        else:
            bestVal = player.eval_fn.score(game, player)
            print(depth, ' 2.1CP')
        bestMove = game.get_player_position(player)
        L1 = list(bestMove)
        L1.append(last_move[2])
        bestMove = tuple(L1)
        # print("Depth :", depth, "Moves :", bestMove, bestVal)
        print(bestMove, bestVal)
        return bestMove, bestVal

    elif (my_turn):
        print(depth, ' 1CP')
        bestVal = -1000
        available_moves = game.get_player_moves(player)
        print(player.__class__.__name__)
        bestMove = (-1, -1, 0)
        forecast = {}
        print(depth, ' 2CP')
        for move in available_moves:
            forecast[game.forecast_move(move)[0]] = move

        for fore in forecast:
            val = minimax(game.get_inactive_player(), fore, time_left, depth - 1, False, forecast[fore])
            if val[1] > bestVal:
                bestVal = val[1]
                bestMove = val[0]
        print(depth, ' 3CP')
        print(bestMove, bestVal)

    else:
        print(depth, ' 1RP')
        bestVal = 1000
        available_moves = game.get_player_moves(player)
        print(player.__class__.__name__)
        bestMove = (-1, -1, 0)
        forecast = {}
        print(depth, ' 2RP')
        for move in available_moves:
            forecast[game.forecast_move(move)[0]] = move

        for fore in forecast:
            val = minimax(game.get_inactive_player(), fore, time_left, depth - 1, True, forecast[fore])
            if val[1] < bestVal:
                bestVal = val[1]
                bestMove = val[0]
        print(depth, ' 3RP')
        print(bestMove, bestVal)

    # print("Depth :", depth, "Moves :", bestMove, bestVal)
    print(depth, ' 1TOT')
    return bestMove, bestVal

    '''
    #(x,x,x), (u,v,w)..
    available_moves = game.get_player_moves(player)

    #game boards for each of the above
    forecast = [game.forecast_move(move)[0] for move in available_moves]

    #-4,2,6...
    score = [player.eval_fn.score(fore,player) for fore in forecast]

    #6
    best_val = max(score)

    #(u,v,w)
    best_move = available_moves[score.index(best_val)]

    print(best_val)
    print(best_move)
    return best_move, best_val
    '''


######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
tests.beatRandom(CustomPlayer)
tests.minimaxTest(CustomPlayer, minimax)
################ END OF LOCAL TEST CODE SECTION ######################