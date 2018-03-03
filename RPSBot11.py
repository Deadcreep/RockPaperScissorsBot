import random

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
        self.lf = 0.9 #фактор обучения
        self.df = 0.5 #фактор дисконтирования. Чем он меньше, тем меньше думает о будущих действий
        self.nuclease = {'RP': 'a', 'PS': 'b', 'SR': 'c', 'PR': 'd', 'SP': 'e', 'RS': 'f', 'RR': 'g', 'PP': 'h',
                         'SS': 'i'}
        self.human_moves = ""
        self.bot_moves = ""
        self.DNAmoves = ""
        self.length = 0
        self.index=-1;
        self.newstate = tuple()
        self.bot_sign = random.choice(['R', 'P', 'S'])

    def bot(self, prev_human_sign, foo=0, foo2=0):

        human_sign = prev_human_sign

        if(human_sign == ""): return random.choice(['0', '2', '1'])
        if prev_human_sign == 0: human_sign = 'R'
        if prev_human_sign == 1: human_sign = 'S'
        if prev_human_sign == 2: human_sign = 'P'
        self.human_moves += human_sign
        self.bot_moves += self.bot_sign
        self.DNAmoves += self.nuclease[human_sign + self.bot_sign]
        self.length += 1
        state = self.newstate
        self.newstate = []

        limit = min([self.length, 5])
        j = limit
        while j >= 1 and not self.DNAmoves[self.length - j : self.length] in self.DNAmoves[0:self.length - 1]:
            j -= 1
        if j >= 1:
            i = self.DNAmoves.rfind(self.DNAmoves[self.length - j:self.length], 0,
                                    self.length - 1)
            self.newstate.append(self.human_moves[j + i])
            self.newstate.append(self.bot_moves[j + i])
        j = limit
        while j >= 1 and not self.human_moves[self.length - j:self.length] in self.human_moves[0:self.length - 1]:
            j -= 1
        if j >= 1:
            i = self.human_moves.rfind(self.human_moves[self.length - j:self.length], 0,
                                       self.length - 1)
            self.newstate.append(self.human_moves[j + i])
            self.newstate.append(self.bot_moves[j + i])
        j = limit
        while j >= 1 and not self.bot_moves[self.length - j:self.length] in self.bot_moves[0:self.length - 1]:
            j -= 1
        if j >= 1:
            i = self.bot_moves.rfind(self.bot_moves[self.length - j:self.length], 0,
                                     self.length - 1)
            self.newstate.append(self.human_moves[j + i])
            self.newstate.append(self.bot_moves[j + i])

        print(f'newstate: {self.newstate}')
        #print(f'state: {state}')
        self.newstate = tuple(self.newstate)
        action = self.bot_sign
        reward = score[(action, human_sign)]
        maxvalue = max(self.Q.get((self.newstate, a), 0) for a in 'RPS')
        self.Q[(state, action)] = self.Q.get((state, action), 0) + self.lf * (
            reward + self.df * maxvalue - self.Q.get((state, action), 0))
        print(f'Q: {self.Q}')
        succ = [self.Q.get((self.newstate, a), 0) for a in 'RPS']
        print(succ)
        optimal_actions = ['RPS'[x] for x in range(len(succ)) if succ[x] == max(succ)]
        print(optimal_actions)
        self.bot_sign = random.choice(optimal_actions) if random.random() > self.epsilon else random.choice('RPS')
        if(self.bot_sign == 'R'): result = 0
        if (self.bot_sign == 'P'): result = 2
        if (self.bot_sign == 'S'): result = 1
        return result

