# export
def minimax(player, game, time_left, depth, my_turn=True, move=(-1, -1, False)):
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

    # print("Active Pos :",game.forecast_move(available_moves[0])[0].get_player_position(player))

    if depth == 0:
        # curr_player = game.get_active_player()
        # print(curr_player.get_name())
        bestVal = len(game.get_player_moves(player)) - len(game.get_opponent_moves(player))
        bestMove = move

    elif (my_turn):
        available_moves = game.get_player_moves(player)
        new_boards = {}
        for move in available_moves:
            new_boards[move] = game.forecast_move(move)[0]
            # print("WTF!!!")
            # print(new_boards[move].get_inactive_position())

        bestVal = -1000
        bestMove = (-1, -1, False)
        for nb in new_boards:
            val = minimax(player, new_boards[nb], time_left, depth - 1, False, nb)
            if val[1] > bestVal:
                bestVal = val[1]
                bestMove = val[0]

    else:
        available_moves = game.get_player_moves(player)
        new_boards = {}
        for move in available_moves:
            new_boards[move] = game.forecast_move(move)[0]
        bestVal = 1000
        bestMove = (-1, -1, False)
        for nb in new_boards:
            val = minimax(player, new_boards[nb], time_left, depth - 1, True, nb)
            if val[1] < bestVal:
                bestVal = val[1]
                bestMove = val[0]

    return bestMove, bestVal


######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
tests.beatRandom(CustomPlayer)
tests.minimaxTest(CustomPlayer, minimax)
################ END OF LOCAL TEST CODE SECTION ######################