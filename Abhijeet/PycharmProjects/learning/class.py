class Enemy:
    life = 3

    def attack(self):
        print("fuck")
        self.life -= 1
    def CheckLife(self):
        if self.life <= 0:
            print('i am dead')
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.CheckLife()

#enemy2.attack()
enemy2.CheckLife()