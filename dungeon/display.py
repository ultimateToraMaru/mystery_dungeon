class Display():

    def show_status(level, hp, max_hp, mp, max_mp, attack, difense):
        print('**********')
        print('Level:', level)
        print('HP:', hp, '/', max_hp)
        print('MP:', mp, '/', max_mp)
        print('Attack:', attack)
        print('Difense', difense)
        print('**********')
    
    def show_number_of_floors(num):
        print(num, '階')