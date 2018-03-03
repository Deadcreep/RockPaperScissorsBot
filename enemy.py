import RPSBot
from random import randrange
#from collections import Counter
import numpy as np

def bot(prev_human_sign=[], prev_round_result=[], round_number=0):
    bot_sign = 0;
    if round_number < 0:
        bot_sign = randrange(3);
        print('\nБот рандом:{0}'.format(bot_sign));
    else:
        c = np.bincount(prev_human_sign)
        player_sign = np.arange(len(c))[c == c.max()].min();

        if prev_round_result[round_number] == 2 or prev_round_result[round_number] == 1:
            bot_sign = getCounterPik(prev_human_sign[round_number]);
            print("Контр-пик ничьи или поражения Бота");
        elif prev_round_result[round_number] == 0:
            print("Контр-пик победы Бота");
            # bot_sign=prev_human_sign[round_number]
            bot_sign = getCounterPik(player_sign);
    return bot_sign;


def getCounterPik(sign):
    if sign==0 : counterPik = 2; print('\nБот выбрал БУМАГА')

    elif sign==1:
            counterPik =0;
            print('\nБот выбрал КАМЕНЬ')

    elif sign==2:
            counterPik =1;
            print('\nБот выбрал НОЖНИЦЫ')
    return counterPik;

def game():
    historyPlayer = [];
    historyResultGame = [];

    #print(menu());

    numberGame = 0;
    countWin = 0;
    countLoose = 0;
    countDraw = 0;
    resultBot='';
    while numberGame < 500:

        print('№ раунда: {0} '.format(numberGame))
        #resultPlayer = player()
        # resultPlayer=bot2()
        resultPlayer = RPSBot.RPSBot().bot(resultBot)
        
        resultBot = bot(historyPlayer, historyResultGame, numberGame - 1)#наш
        historyPlayer.append(resultPlayer);

        if resultBot == resultPlayer:
            print('НИЧЬЯ')
            historyResultGame.append(2)
            countDraw += 1;


        elif resultPlayer == 1 and resultBot == 2 or resultPlayer == 0 and resultBot == 1 or resultPlayer == 2 and resultBot == 0:
            print('Игрок победил')
            historyResultGame.append(1);

            countWin += 1;

        else:
            historyResultGame.append(0)
            print('БОТ победил!!')
            countLoose += 1;

        numberGame += 1;

    print('Победы- {0}\n  Поражений - {1}\n Ничьи- {2}'.format(countWin, countLoose, countDraw));

if __name__ == "__main__":
    game();