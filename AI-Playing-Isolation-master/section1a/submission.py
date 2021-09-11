
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: notebook.ipynb

import time
from isolation import Board

# Credits if any
# 1)
# 2)
# 3)

class OpenMoveEvalFn:
    def score(self, game, my_player=None):
        """Score the current game state
        Evaluation function that outputs a score equal to how many
        moves are open for AI player on the board minus how many moves
        are open for Opponent's player on the board.

        Note:
            If you think of better evaluation function, do it in CustomEvalFn below.

            Args
                game (Board): The board and game state.
                my_player (Player object): This specifies which player you are.

            Returns:
                float: The current state's score. MyMoves-OppMoves.

            """

        # TODO: finish this function!

        return len(game.get_player_moves(my_player)) - len(game.get_opponent_moves(my_player))

######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
################ END OF LOCAL TEST CODE SECTION ######################

class CustomPlayer:
    # TODO: finish this class!
    """Player that chooses a move using your evaluation function
    and a minimax algorithm with alpha-beta pruning.
    You must finish and test this player to make sure it properly
    uses minimax and alpha-beta to return a good move."""

    def __init__(self, search_depth=3, eval_fn=OpenMoveEvalFn()):
        """Initializes your player.

        if you find yourself with a superior eval function, update the default
        value of `eval_fn` to `CustomEvalFn()`

        Args:
            search_depth (int): The depth to which your agent will search
            eval_fn (function): Evaluation function used by your agent
        """
        self.name = "CustomPlayer"
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, time_left):
        """Called to determine one move by your agent

        Note:
            1. Do NOT change the name of this 'move' function. We are going to call
            this function directly.
            2. Call alphabeta instead of minimax once implemented.
        Args:
            game (Board): The board and game state.
            time_left (function): Used to determine time left before timeout

        Returns:
            tuple: (int,int,bool): Your best move
        """
        best_move, utility = minimax(self, game, time_left, depth=self.search_depth)
        return best_move

    def utility(self, game, my_turn):
        """You can handle special cases here (e.g. endgame)"""
        return self.eval_fn.score(game, self)

    def get_name(self):
        return self.name
###################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE CLASS! ################
###### IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ###########
###################################################################

def minimax(player, game, time_left, depth, my_turn=True):
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


    if depth==0:
        if(not my_turn):
            curr_player = game.get_inactive_player()
        else:
            curr_player = player

        bestVal = len(game.get_player_moves(curr_player)) - len(game.get_opponent_moves(curr_player))
        bestMove = (-1,-1,False)
        #print("Value turn. Depth :", depth)
        #print(game.get_player_position(curr_player), bestVal)


    elif(my_turn):

        #print("Max turn start. Depth :", depth)
        bestVal = float("-inf")
        bestMove = (-1,-1,False)
        available_moves = game.get_player_moves(player)
        #print(available_moves)
        for move in available_moves:
            val = minimax(game.get_inactive_player(), game.forecast_move(move)[0], time_left, depth-1, False)
            if val[1]>bestVal:
                bestVal = val[1]
                bestMove = move
            if time_left() <20:
                break
        #print("Max turn end. Depth :", depth)
        #print(bestMove, bestVal)
        #return bestMove, bestVal

    else:
        #print("Min turn start. Depth :", depth)
        available_moves = game.get_player_moves(player)
        #print(available_moves)
        bestVal = float("inf")
        bestMove = (-1,-1,False)
        for move in available_moves:
            val = minimax(game.get_inactive_player(), game.forecast_move(move)[0], time_left, depth-1, True)
            if val[1]<bestVal:
                bestVal = val[1]
                bestMove = move
            if time_left() <20:
                break
        #print("Min turn end. Depth :", depth)
        #print(bestMove, bestVal)
        #return bestMove, bestVal

    return bestMove, bestVal

######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
################ END OF LOCAL TEST CODE SECTION ######################

def alphabeta(player, game, time_left, depth, alpha=float("-inf"), beta=float("inf"), my_turn=True):
    """Implementation of the alphabeta algorithm.

    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you need
            from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer())
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        alpha (float): Alpha value for pruning
        beta (float): Beta value for pruning
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """
    # TODO: finish this function!
    raise NotImplementedError
    return best_move, val


######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
# tests.name_of_the_test #you can uncomment this line to run your test
################ END OF LOCAL TEST CODE SECTION ######################

class CustomEvalFn:
    def __init__(self):
        pass

    def score(self, game, my_player=None):
        """Score the current game state.

        Custom evaluation function that acts however you think it should. This
        is not required but highly encouraged if you want to build the best
        AI possible.

        Args:
            game (Board): The board and game state.
            my_player (Player object): This specifies which player you are.

        Returns:
            float: The current state's score, based on your own heuristic.
        """

        # TODO: finish this function!
        raise NotImplementedError

######################################################################
############ DON'T WRITE ANY CODE OUTSIDE THE CLASS! #################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################