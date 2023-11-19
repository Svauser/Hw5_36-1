import random
from random import randint
def slot (my_num,bid,bank):

        i = randint(1,30)
        if i==my_num:
            print('ВЫ в выигрыше')
            return (bank + bid)
        else:

            print('Вы в проигрыше')
            return (bank - bid)



