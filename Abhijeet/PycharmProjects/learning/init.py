'''class Tuna:

    def __init__(self):
        print('ssup tuna')
    def swim(self):
        print('i am swimming')


flipper = Tuna()

#flipper.swim()'''

class Enemy:
    def __init__(self, x):
        self.energy = x
        print(self.energy)
    def get_energy_level(self):
       print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)


jason.get_energy_level()
sandy.get_energy_level()