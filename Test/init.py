class Enemy:

    def __init__(self, x):
        self.energy =x
        print('Constructor')

    def get_energy(self):
        print(self.energy)

json = Enemy(5)


json.get_energy()
