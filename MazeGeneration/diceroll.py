from random import choice

def dice_roll(numb_of_choices:list):
    '''
    :param numb_of_choices:
    :return: cosen  --- is universal
    '''
    chosen = choice(numb_of_choices)
    return chosen

if __name__ == '__diceroll__':
    dice_roll()
