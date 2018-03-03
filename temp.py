
import RPSBot
from RPSBot import score
import random

class Results:
    def __init__(self):
        self.nwin = 0
        self.ntie = 0
        self.nloss = 0
        self.total_points = 0

    def check_scores(self, human_sign, bot_sign):
        if score[(human_sign, bot_sign)] == 1:
            self.nloss += 1
        elif score[(human_sign, bot_sign)] == 0:
            self.ntie += 1
        elif score[(human_sign, bot_sign)] == -1:
            self.nwin += 1
        self.total_points = self.nwin - self.nloss
        print(f'Wins: {self.nwin}, Lose: {self.nloss}, Ties: {self.ntie}, Total points: {self.total_points}')


if __name__ == "__main__":
    bot1 = RPSBot.RPSBot()
    bot2 = RPSBot.RPSBot()
    turn_number = 0
    history = Results()
    human_sign = ""
    bot2_s = ""
    #while True:
    for i in range(1, 100000):
        print(f'Turn № {turn_number}')
        turn_number += 1
        bot_sign = bot1.bot(human_sign)
        #human_sign = input("Enter your sign: ").upper()
        human_sign = random.choice(['R', 'S'])
        #bot1_s = bot1.bot(bot2_s)
        #bot2_s = bot2.bot(bot1_s)
        #human_sign = random.choice(['R', 'P', 'S'])
        print(f'Bot choice: {bot_sign}')
        history.check_scores(human_sign=human_sign, bot_sign=bot_sign)
        #history.check_scores(bot1_s, bot2_s)
        print('---------------------------')
