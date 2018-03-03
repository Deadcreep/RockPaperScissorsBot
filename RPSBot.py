import random

"""Коды для жестов:
    0 — камень
    1 — ножницы
    2 — бумага

    Камень побеждает ножницы («камень затупляет или ломает ножницы»).
    Бумага побеждает камень («бумага накрывает камень»).
    Ножницы побеждают бумагу («ножницы разрезают бумагу»).

    Коды результатов раунда:
    0 — ничья
    1 — выиграл человек
    2 — выиграл бот

    Код вознаграждения
    1 - выиграл бот
    0 - ничья
    -1 - проигрыш
    
prev_human_sign - предыдущий жест 
prev_round_result – результат предыдущего раунда
round_number – номер текущего (k-ого) раунда,  
bot_sign – выбранный ботом жест в текущем (k-ом) раунде"""
score = {
            ('R', 'R'): 0, ('R', 'P'): -1, ('R', 'S'): 1,
            ('P', 'R'): 1, ('P', 'P'): 0, ('P', 'S'): -1,
            ('S', 'R'): -1, ('S', 'P'): 1, ('S', 'S'): 0
        }


class RPSBot:
    def __init__(self):
        self.epsilon = 0.2
        self.begin_flag = True
        self.Q = dict()
        self.lr = 0.9
        # self.limits = [5, 15, 30]
        self.beat = {'R': 'P', 'P': 'S', 'S': 'R'}
        self.nuclease = {'RP': 'a', 'PS': 'b', 'SR': 'c', 'PR': 'd', 'SP': 'e', 'RS': 'f', 'RR': 'g', 'PP': 'h',
                         'SS': 'i'}
        self.human_moves = ""
        self.bot_moves = ""
        self.DNAmoves = ""
        self.length = 0
        self.newstate = tuple()

    def bot(self, prev_human_sign):
        human_sign = prev_human_sign

        bot_sign = random.choice(['R', 'P', 'S'])

        if human_sign == "":
            return bot_sign
        self.human_moves += human_sign
        self.bot_moves += bot_sign
        self.DNAmoves += self.nuclease[human_sign + bot_sign]
        self.length += 1
        state = self.newstate
        self.newstate = []

        limit = min([self.length, 5])
        j = limit
        while j >= 1 and not self.DNAmoves[self.length - j:self.length] in self.DNAmoves[0:self.length - 1]:
            j -= 1
        if j >= 1:
            i = self.DNAmoves.rfind(self.DNAmoves[self.length - j:self.length], 0,
                                    self.length - 1)  # You seem to be playing based on our moves
            self.newstate.append(self.human_moves[j + i])
            self.newstate.append(self.bot_moves[j + i])
        j = limit
        while j >= 1 and not self.human_moves[self.length - j:self.length] in self.human_moves[0:self.length - 1]:
            j -= 1
        if j >= 1:
            i = self.human_moves.rfind(self.human_moves[self.length - j:self.length], 0,
                                       self.length - 1)  # You seem to be playing based on your moves
            self.newstate.append(self.human_moves[j + i])
            self.newstate.append(self.bot_moves[j + i])
        j = limit
        while j >= 1 and not self.bot_moves[self.length - j:self.length] in self.bot_moves[0:self.length - 1]:
            j -= 1
        if j >= 1:
            i = self.bot_moves.rfind(self.bot_moves[self.length - j:self.length], 0,
                                     self.length - 1)  # You seem to be playing based on my moves
            self.newstate.append(self.human_moves[j + i])
            self.newstate.append(self.bot_moves[j + i])

        print(f'newstate: {self.newstate}')
        print(f'state: {state}')
        self.newstate = tuple(self.newstate)
        action = bot_sign
        reward = score[(action, human_sign)]
        maxvalue = max(self.Q.get((self.newstate, a), 0) for a in 'RPS')
        self.Q[(state, action)] = self.Q.get((state, action), 0) + self.lr * (
            reward + 0.5 * maxvalue - self.Q.get((state, action), 0))
        print(f'Q: {self.Q}')
        succ = [self.Q.get((self.newstate, a), 0) for a in 'RPS']
        optimal_actions = ['RPS'[x] for x in range(len(succ)) if succ[x] == max(succ)]
        bot_sign = random.choice(optimal_actions) if random.random() > self.epsilon else random.choice('RPS')
        return bot_sign

