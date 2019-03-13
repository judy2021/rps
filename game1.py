from random import randint


class Player:
    """The Player class is the parent class for all of the Players
    in this game"""
    moves = ['rock', 'paper', 'scissors']

    def move(self, my_move, opp_move):
        return my_move

    def recall(self, my_move, opp_move):
        """
        Inputs:
            my_move (str): 'rock' 'paper' or 'scissors'
            opp_move (str): 'rock' 'paper' or 'scissors'
        Outputs:
            my_move (str): 'rock' 'paper' or 'scissors'
            opp_move (str): 'rock' 'paper' or 'scissors'
        """
        print(f"Your opponent played {opp_move} in the previous round.")
        return my_move, opp_move


class Human(Player):
    def move(self, my_move, opp_move):
        hmove = input("What's your play? ").lower()
        while hmove not in self.moves:
            hmove = input("What's your play? ").lower()
        return hmove


class Rocker(Player):
    def move(self, my_move, opp_move):
        return 'rock'


class Randomizer(Player):
    def move(self, my_move, opp_move):
        return self.moves[randint(0, len(self.moves)-1)]


class Copycat(Player):
    """
    Given the opposing player's previous move,
    imitate that move for this round.
    """
    def move(self, my_move, opp_move):
        if opp_move == 'rock':
            return 'rock'
        if opp_move == 'paper':
            return 'paper'
        else:
            return 'scissors'


class Cycler(Player):
    """
    Given the Cycler's previous move,
    continue to the next move in the cycle.
    Ex: Rock -> Paper -> Scissors -> Rock -> ... """
    def move(self, my_move, opp_move):
        if my_move == 'rock':
            return self.moves[1]  # paper
        if my_move == 'paper':
            return self.moves[2]  # scissors
        else:
            return self.moves[0]  # rock


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def winner(self, p1_move, p2_move):
        """
        Inputs:
            p1_move (str): Player 1's move
            p2_move (str): Player 2's move
        Outputs:
            Winner: Print whether player 1 or 2 won
            Winner (int): 0 for tie, 1 for player 1, 2 for player 2
        Purpose:
            Compute the winner of a round.
        """
        if p1_move == p2_move:
            return "No winner.\n", 0  # no winner
        elif ((p1_move == 'rock' and p2_move == 'scissors') or
              (p1_move == 'scissors' and p2_move == 'paper') or
              (p1_move == 'paper' and p2_move == 'rock')):
            print("Player 1 wins!\n")
            return 1  # player 1
        else:
            print("Player 2 wins!\n")
            return 2  # player 2

    def scoreboard(self, rnd_winner, prev_p1_score, prev_p2_score):
        """
        Inputs:
            rnd_winner (int): 1 for player 1, 2 for player 2
            prev_p1_score (int): Previous score for player 1
            prev_p2_score (int): Previous score for player 2
        Outputs:
            Scoreboard: display of current player scores
            p1_score (int): Player 1's updated score
            p2_score (int): Player 2's updated score
        Purpose:
            Display a scoreboard of the game and
            return the updated player scores.
        """
        if rnd_winner == 1:
            new_p1_score = prev_p1_score + 1
            print(f" Score\n {new_p1_score} | {prev_p2_score}\n-----")
            return new_p1_score, prev_p2_score
        elif rnd_winner == 2:
            new_p2_score = prev_p2_score + 1
            print(f" Score\n {prev_p1_score} | {new_p2_score}\n-----")
            return prev_p1_score, new_p2_score
        else:
            print(f" Score\n {prev_p1_score} | {prev_p2_score}\n-----")
            return prev_p1_score, prev_p2_score

    def final_score(self, p1_score, p2_score):
        """
        Inputs:
            p1_score (int): Player 1's score
            p2_score (int): Player 2's score
        Outputs: Display scoreboard and winner text.
        Purpose: Display the final score for each player in a scoreboard.
        """
        print(f"\nFinal Score\n  {p1_score} | {p2_score}\n --------")
        if p1_score > p2_score:
            print('Congratulations to Player 1!')
        if p1_score < p2_score:
            print('Congratulations to Player 2!')
        else:
            print("It's a draw!")

    def play_round(self, current_rnd, final_rnd, prev_p1_move, prev_p2_move):
        """
        Inputs:
            current_rnd (int):
            final_rnd (int):
        Outputs:
            p1_move (str): Player 1's move
            p2_move (str): Player 2's move
        Purpose:
            Print and return the moves of two players.
        """
        if current_rnd == 1:
            p1_move = self.p1.move()
            p2_move = self.p2.move()
            print(f"Player 1: {p1_move} \nPlayer 2: {p2_move}\n-----")
            return p1_move, p2_move
        else:
            p1_move = self.p1.move(prev_p1_move, prev_p2_move)
            p2_move = self.p2.move(prev_p1_move, prev_p2_move)
            print(f"Player 1: {p1_move} \nPlayer 2: {p2_move}\n-----")
            return p1_move, p2_move

    def play_match(self):
        """
        Inputs: total_rnds
        Outputs: None
        Purpose:
          Play a match of several rounds. User selects the number of rounds.
        """
        rounds = int(input('How many rounds do you want to play? '))
        print("Let's begin!\n")
        p1_score, p2_score = 0, 0
        # default starting moves for Players that require one
        

        for round in range(1, rounds+1):  # non-technical counting
            print(f"\n..........\n Round {round}\n..........\n")
            p1_move, p2_move = self.play_round(round, rounds,
            winning_p = self.winner(p1_move, p2_move), 
            p1_score, p2_score = self.scoreboard(winning_p, p1_score, p2_score)
                 (prev_p1_move),prev_p2_move = self.p1.recall(p1_move, p2_move)
                 (prev_p2_move), p1_opp_move = self.p2.recall(p2_move, p1_move)
                 (self).final_score(p1_score, p2_score)
                 (print)("\nGame over.")

       
       


(player_pool_text)(" You may choose from the following player pool,Human: you control the moves, Rocker: computer that always chooses rock,Randomizer: computer that moves randomly,Copycat: computer that imitates the opponent's previous move, Cycler: computer that cycles through rock, paper, and scissors")

if __name__ == '__main__'
   ( player_pool )=={'human': Human,
                   'rocker': Rocker,
                   'randomizer': Randomizer,
                   'copycat': Copycat,
                   'cycler': Cycler}
    (print)(player_pool_text)
    (player1 )== input("Who is Player 1?").lower()
    (player2) == input("Who is Player 2?").lower()

    game == (Game)(player_pool[player1], player_pool[player2])
    game.play_match